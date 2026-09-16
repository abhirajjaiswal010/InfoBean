Python webbrowser Module

The webbrowser module is a Python built-in module used to open web pages and URLs in the user's default web browser.

No installation required.

import webbrowser
1. Main Methods
Method	What it does	Example
open()	Opens a URL in the default browser	webbrowser.open("https://google.com")
open_new()	Opens a URL in a new browser window	webbrowser.open_new("https://google.com")
open_new_tab()	Opens a URL in a new browser tab	webbrowser.open_new_tab("https://google.com")
get()	Gets a browser controller object	webbrowser.get()
register()	Registers a browser type manually	webbrowser.register(...)
get().open()	Opens URL using a specific browser controller