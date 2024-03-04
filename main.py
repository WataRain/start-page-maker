import os
import json
from tkinter import Tk
from tkinter import Frame, LabelFrame, Label, Entry, Menu
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import StringVar

TITLE = "Start Page Maker by waflrain (2024)"
SUBTITLE = "Submitted as a final project in Harvard's CS50x 2024 course"
OUTPUT_START = """<!DOCTYPE html>
<html>
<head>
    <title>Generated Start Page</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <nav>
    <h1>Start</h1>
    <ul>
"""
OUTPUT_END = "    </ul>\n</nav>\n</body>\n</html>"
class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.wm_title(TITLE)
        self.wm_geometry("600x300")
        self.wm_resizable(False, False)
        self.data = []

        menubar = Menu(self)
        menubar.add_command(label="Save to JSON",   command=self.data_to_json)
        menubar.add_command(label="Load from JSON", command=self.json_to_data)
        menubar.add_command(label="Export to HTML", command=self.data_to_html)
        self.config(menu=menubar)

        frame_title = Frame(self)
        Label(frame_title, text=TITLE, font=("Segoe UI", 14)).pack()
        Label(frame_title, text=SUBTITLE).pack()
        frame_title.pack()

        frame_entries = LabelFrame(self, text="Set URLs and titles")
        Label(frame_entries, text="Title",).grid(row=0, column=0)
        Label(frame_entries, text="URL").grid(row=0, column=1)
        for i in range(1, 11): # TODO: make this dynamic
            self.data.append({"title": StringVar(self, name=f"Name_{i}"), "url": StringVar(self, name=f"URL_{i}")})
            entry_name = Entry(frame_entries, width=32, textvariable=self.data[i-1]["title"])
            entry_name.grid(row=i, column=0)
            entry_url = Entry(frame_entries, width=64, textvariable=self.data[i-1]["url"])
            entry_url.grid(row=i, column=1)
        frame_entries.pack()

        print("Welcome to Start Page Maker!")


    def data_to_html(self):
        out_html = OUTPUT_START
        print("TITLE\t\t\tURL")
        for datum in self.data:
            print(datum["title"].get() + "\t\t\t" + datum["url"].get())
            if datum["title"].get() and datum["url"].get():
                out_html += f"        <li><a href={datum['url'].get()}>{datum['title'].get()}</li>\n"
        out_html += OUTPUT_END
        filename = asksaveasfilename(title="Export to HTML", confirmoverwrite=True, defaultextension=".html", filetypes=[("HTML", '.html')], initialdir=os.getcwd())
        with open(filename, "w") as textfile:
            textfile.write(out_html)
        return


    def data_to_json(self):
        data_string_values = [{'title': datum['title'].get(), 'url': datum['url'].get()} for datum in self.data]
        filename = asksaveasfilename(title="Save to JSON", confirmoverwrite=True, defaultextension=".json", filetypes=[("JSON", '.json')], initialdir=os.getcwd())
        with open(filename, "w") as textfile:
            textfile.write(json.dumps(data_string_values, indent=4))
        return


    def json_to_data(self):
        filename = askopenfilename(title="Load from JSON", defaultextension=".json", filetypes=[("JSON", '.json')], initialdir=os.getcwd())
        with open(filename, "r") as textfile:
            data_string_values = json.loads(textfile.read())
        for i in range(len(self.data)):
            self.data[i]["title"].set(data_string_values[i]["title"])
            self.data[i]["url"].set(data_string_values[i]["url"])
        return


if __name__ == "__main__":
    app = App()
    app.mainloop()
