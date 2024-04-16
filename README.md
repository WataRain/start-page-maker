# Simple Start Page Maker

#### Video Demo: <https://www.youtube.com/watch?v=zLNRZojZTgg>

#### Description:

Simple Start Page Maker is a program written in Python that lets the user
generate HTML representing a bookmarks page through a Tkinter-based GUI.
Start page configurations can also be saved to or loaded from JSON.

To use the application, first input the names and URLs of the websites you wish
to "bookmark". Optionally, you may also set a custom text color and a background
color by clicking on any of the two buttons at the bottom and choosing a color
from the color picker. Finally, click on "Export to HTML" to indeed generate
valid HTML that can then be used with any web browser. If wanting to save a
configuration for later, you may "Save to JSON" and "Load to JSON" through the
menu buttons of the same name. (JSON, or JavaScript Object Notation, is a
well-recognized file format that I used in order to simplify storing and
retrieving the data used in this program.)

The project was born out of a desire to add more personalization to web
browsers. Honestly, we could easily just add another bookmark in the default
start page, but it would be cooler if we could have our own custom-made start
page. Many tutorials exist online for this, some of which I've followed in the
past to create my own beautiful start pages. At the same time, however, some
people may want in on the action, yet may not have enough time to manually code
everything from scratch. Hence, the idea to automate at least some part of the
process came into being as Simple Start Page Maker.

The app was written in the Python programming language and makes extensive use
of the Tkinter module. Tkinter is a GUI toolchain framework that simplifies GUI
development by defining various "widgets" (e.g., Labels, Entries, Buttons,
Frames, etc.) that can be instantiated, configured, and combined to create
simple but functional GUIs.

This project can be expanded to customize other aspects of the page, such as the
title and the big "Start" header. It would be easy, too: all anyone would need
to do is add two more Entries (perhaps in a LabelFrame) and add the needed
functionality.
