import os
import json
from tkinter import Tk
from tkinter import Frame, LabelFrame, Label, Entry, Menu, Button
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.colorchooser import askcolor
from tkinter import StringVar
from bs4 import BeautifulSoup
from constants import *


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.wm_title(TITLE)
        self.wm_geometry("570x390")
        self.wm_resizable(False, False)
        self.data = {
            "sites": [],
            "text_color": StringVar(self, NO_TEXTCOLOR, "Text_Color"),
            "bg_color": StringVar(self, NO_BGCOLOR, "BG_Color")
            }

        menubar = Menu(self)
        menubar.add_command(label="Save to JSON",   command=self.data_to_json)
        menubar.add_command(label="Load from JSON", command=self.json_to_data)
        menubar.add_command(label="Export to HTML", command=self.data_to_html)
        self.config(menu=menubar)

        frame_title = Frame(self)
        Label(frame_title, text=TITLE, font=("Segoe UI", 14)).pack()
        Label(frame_title, text=SUBTITLE).pack()
        frame_title.pack(pady=10)

        frame_entries = LabelFrame(self, text="Set URLs and titles")
        Label(frame_entries, text="Title").grid(row=1, column=0)
        Label(frame_entries, text="URL").grid(row=1, column=1)
        for i in range(0, 10): # TODO: make this dynamic
            self.data["sites"].append(
                {
                    "title": StringVar(self, name=f"Name_{i}"),
                    "url": StringVar(self, name=f"URL_{i}")
                }
                )
            Entry(frame_entries, width=32, textvariable=self.data["sites"][i]["title"]).grid(row=i+2, column=0)
            Entry(frame_entries, width=40, textvariable=self.data["sites"][i]["url"]).grid(row=i+2, column=1)
        frame_entries.pack()

        frame_color = LabelFrame(self, text="Color")
        frame_textcolor = LabelFrame(frame_color, text="Text Color")
        Button(frame_textcolor, textvariable=self.data["text_color"], command=self.set_text_color).pack()
        frame_textcolor.pack(side="left")
        frame_bgcolor = LabelFrame(frame_color, text="Back Color")
        Button(frame_bgcolor, textvariable=self.data["bg_color"], command=self.set_bg_color).pack()
        frame_bgcolor.pack(side="right")
        frame_color.pack()

        print("Welcome to Start Page Maker!")


    def set_color(self, key):
        color = askcolor(self.data[key].get())
        print(color)
        if color[0] is not None:
            self.data[key].set(color[1])
        return


    def set_text_color(self):
        self.set_color("text_color")
        return


    def set_bg_color(self):
        self.set_color("bg_color")
        return


    def data_to_html(self):
        out_html = HTML
        list_html = ""
        print("TITLE\t\t\tURL")
        for datum in self.data["sites"]:
            print(datum["title"].get() + "\t\t\t" + datum["url"].get())
            if datum["title"].get() and datum["url"].get():
                list_html += f"<li><a href={datum['url'].get()}>{datum['title'].get()}</li>\n"
        out_html = out_html.replace("$$ INSERT CONTENT HERE $$", list_html)
        out_html = out_html.replace("$$ BACKGROUND COLOR $$", self.data["bg_color"].get())
        out_html = out_html.replace("$$ TEXT COLOR $$", self.data["text_color"].get())
        soup = BeautifulSoup(out_html, features="html.parser")
        out_html = soup.prettify()
        filename = asksaveasfilename(title="Export to HTML", confirmoverwrite=True, defaultextension=".html", filetypes=[("HTML", '.html')], initialdir=os.getcwd())
        with open(filename, "w") as textfile:
            textfile.write(out_html)
        return


    def data_to_json(self):
        data_json = {
            "sites": [{'title': datum['title'].get(), 'url': datum['url'].get()} for datum in self.data["sites"]],
            "text_color": self.data["text_color"].get(),
            "bg_color": self.data["bg_color"].get(),
            }
        filename = asksaveasfilename(title="Save to JSON", confirmoverwrite=True, defaultextension=".json", filetypes=[("JSON", '.json')], initialdir=os.getcwd())
        with open(filename, "w") as textfile:
            textfile.write(json.dumps(data_json, indent=4))
        return


    def json_to_data(self):
        filename = askopenfilename(title="Load from JSON", defaultextension=".json", filetypes=[("JSON", '.json')], initialdir=os.getcwd())
        with open(filename, "r") as textfile:
            data_str = json.loads(textfile.read())
        self.data["text_color"].set(data_str["text_color"])
        self.data["bg_color"].set(data_str["bg_color"])
        for i in range(len(self.data["sites"])):
            self.data["sites"][i]["title"].set(data_str["sites"][i]["title"])
            self.data["sites"][i]["url"].set(data_str["sites"][i]["url"])
        return


if __name__ == "__main__":
    app = App()
    app.mainloop()
