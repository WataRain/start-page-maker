import os
import json
from tkinter import Tk
from tkinter import Frame, LabelFrame, Label, Entry, Menu
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import StringVar
from bs4 import BeautifulSoup
from constants import *

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.wm_title(TITLE)
        self.wm_geometry("550x400")
        self.wm_resizable(False, False)
        self.data = {"sites": [], "text_color": [], "bg_color": []}

        menubar = Menu(self)
        menubar.add_command(label="Save to JSON",   command=self.data_to_json)
        menubar.add_command(label="Load from JSON", command=self.json_to_data)
        menubar.add_command(label="Export to HTML", command=self.data_to_html)
        self.config(menu=menubar)

        frame_title = Frame(self)
        Label(frame_title, text=TITLE, font=("Segoe UI", 14)).pack()
        Label(frame_title, text=SUBTITLE).pack()
        frame_title.grid(row=0, column=0)

        frame_entries = LabelFrame(self, text="Set URLs and titles")
        Label(frame_entries, text="Title",).grid(row=0, column=0)
        Label(frame_entries, text="URL").grid(row=0, column=1)
        for i in range(0, 10): # TODO: make this dynamic
            self.data["sites"].append(
                {
                    "title": StringVar(self, name=f"Name_{i}"),
                    "url": StringVar(self, name=f"URL_{i}")
                }
                )
            Entry(frame_entries, width=32, textvariable=self.data["sites"][i]["title"]).grid(row=i, column=0)
            Entry(frame_entries, width=48, textvariable=self.data["sites"][i]["url"]).grid(row=i, column=1)
        frame_entries.grid(row=1, column=0)

        frame_color = LabelFrame(self, text="Color")
        frame_textcolor = LabelFrame(frame_color, text="Text Color")
        frame_bgcolor = LabelFrame(frame_color, text="Back Color")
        # TODO: Restrict inputs to integers only. Don't forget to allow the user
        # to delete the inputs as well.
        # TODO: It may be easier to use `tkinter colorchooser.askcolor()`
        for i, color in enumerate(COLORS):
            self.data["text_color"].append(StringVar(self, name=f"text_{color}"))
            Label(frame_textcolor, text=color).grid(row=i, column=0)
            Entry(frame_textcolor, textvariable=self.data["text_color"][i]).grid(row=i, column=1)
            self.data["bg_color"].append(StringVar(self, name=f"bg_{color}"))
            Label(frame_bgcolor, text=color).grid(row=i, column=0)
            Entry(frame_bgcolor, textvariable=self.data["bg_color"][i]).grid(row=i, column=1)
        frame_textcolor.pack(side="left")
        frame_bgcolor.pack(side="right")
        frame_color.grid(row=2, column=0)

        # Everything is done initializing.
        print("Welcome to Start Page Maker!")

    # TODO: Include color data
    def data_to_html(self):
        out_html = OUTPUT_START
        print("TITLE\t\t\tURL")
        for datum in self.data["sites"]:
            print(datum["title"].get() + "\t\t\t" + datum["url"].get())
            if datum["title"].get() and datum["url"].get():
                out_html += f"<li><a href={datum['url'].get()}>{datum['title'].get()}</li>\n"
        out_html += OUTPUT_END
        soup = BeautifulSoup(out_html, features="html.parser")
        out_html = soup.prettify()
        filename = asksaveasfilename(title="Export to HTML", confirmoverwrite=True, defaultextension=".html", filetypes=[("HTML", '.html')], initialdir=os.getcwd())
        with open(filename, "w") as textfile:
            textfile.write(out_html)
        return


    def data_to_json(self):
        data_json = {
            "sites": [{'title': datum['title'].get(), 'url': datum['url'].get()} for datum in self.data["sites"]],
            "bg_color":[int(color.get()) for color in self.data["bg_color"]]
            }
        filename = asksaveasfilename(title="Save to JSON", confirmoverwrite=True, defaultextension=".json", filetypes=[("JSON", '.json')], initialdir=os.getcwd())
        with open(filename, "w") as textfile:
            textfile.write(json.dumps(data_json, indent=4))
        return


    # TODO: Include color data
    def json_to_data(self):
        filename = askopenfilename(title="Load from JSON", defaultextension=".json", filetypes=[("JSON", '.json')], initialdir=os.getcwd())
        with open(filename, "r") as textfile:
            data_string_values = json.loads(textfile.read())
        for i in range(len(self.data["sites"])):
            self.data["sites"][i]["title"].set(data_string_values["sites"][i]["title"])
            self.data["sites"][i]["url"].set(data_string_values["sites"][i]["url"])
        return


if __name__ == "__main__":
    app = App()
    app.mainloop()
