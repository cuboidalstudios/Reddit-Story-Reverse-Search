import customtkinter as ctk
from datetime import datetime
import webbrowser
import urlParser
import subprocess

import common

class GUI:
    def __init__(self):
        with open("log", "w") as f:
            f.write("----RedditVidReverseSearch----\n")

        with open("link", "w") as f:
            f.write("")

        self.root = ctk.CTk()

        self.root.geometry('500x500')
        self.root.title('Reddit Vid Reverse Search')
        self.root.resizable(False, False)

        self.entry = ctk.CTkEntry(self.root, placeholder_text='enter video link', width=300)

        self.button = ctk.CTkButton(self.root, text='enter', command=self.enterButton, fg_color="grey20",
                                    hover_color='grey10')

        self.button2 = ctk.CTkButton(self.root, text='copy link', command=self.copyLink, fg_color="grey20",
                                     hover_color='grey10')

        self.button3 = ctk.CTkButton(self.root, text='open site', command=self.openSite, fg_color="grey20",
                                     hover_color='grey10')

        self.textLog = ctk.CTkTextbox(self.root, state="disabled", activate_scrollbars=False, height=150, width=460)

        self.outputBox = ctk.CTkTextbox(self.root, state="disabled", height=150, width=460)

    def update(self):
        self.root.after(1000, self.update)
        self.textLog.configure(state="normal")
        with open("log", "r") as f:
            self.textLog.delete(1.0, "end")
            self.textLog.insert(1.0, f.read())
        self.textLog.configure(state="disabled")

        self.outputBox.configure(state="normal")
        with open("link", "r") as f:
            self.outputBox.delete(1.0, "end")
            self.outputBox.insert(1.0, f.read())
        self.outputBox.configure(state="disabled")

    def mainloop(self):
        self.outputBox.place(x=20, y=170)
        self.textLog.place(x=20, y=325)
        self.button.place(x=320, y=10)
        self.button2.place(x=335, y=130)
        self.button3.place(x=25, y=130)
        self.entry.place(x=10, y=10)
        self.root.mainloop()

    def enterButton(self):
        import common
        common.changeLog("enter button")
        text = self.entry.get()
        urlParser.urlParser(text)
        self.root.update()

    def copyLink(self):
        with open("link", "r") as f:
            t = f.read()

        if t != "":
            cmd = "echo " + t.strip() + '|clip'
            common.changeLog("SITE LINK COPIED")
            return subprocess.check_call(cmd, shell=True)

    def openSite(self):
        with open("link", "r") as f:
            l = f.read()
            if l != "":
                webbrowser.open(l)
                common.changeLog("WEBSITE LINK OPENED")
