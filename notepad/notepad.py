from textwrap import fill
import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import font
from turtle import width

from numpy import size

class Notepad:

    __root = Tk()

    # default window width and height
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
    __thisFormatMenu = Menu(__thisMenuBar, tearoff=0)
    __thisFontMenu = Menu(__thisFormatMenu, tearoff=0)

    # add scrollbar
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None

    def __init__(self, **kwargs):

        # Set icon
        try:
            self.__root.wm_iconbitmap("Notepad.ico")
        except:
            pass

        # Set window size

        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        # Set window text
        self.__root.title("Untitled - Notepad")

        # Center window
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        left = (screenWidth / 2) - (self.__thisWidth / 2)

        top = (screenHeight / 2) - (self.__thisHeight / 2)

        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,
            self.__thisHeight,
            left, top))

        # Make textarea auto resizable
        self.__root.grid_rowconfigure(0, weight = 1)
        self.__root.grid_columnconfigure(0, weight = 1)

        # Add controls
        self.__thisTextArea.grid(sticky = N + E + S + W)

        # Open new file
        self.__thisFileMenu.add_command(label = "New", command = self.__newFile)

        # Open existing file
        self.__thisFileMenu.add_command(label = "Open", command = self.__openFile)

        # Save current file
        self.__thisFileMenu.add_command(label = "Save", command = self.__saveFile)

        # Create a line in the dialogue
        self.__thisFileMenu.add_separator()

        # Terminate
        self.__thisFileMenu.add_command(label = "Exit", command = self.__quitApplication)
        self.__thisMenuBar.add_cascade(label = "File", menu = self.__thisFileMenu)

        # Cut
        self.__thisEditMenu.add_command(label = "Cut", command = self.__cut)

        # Copy
        self.__thisEditMenu.add_command(label = "Copy", command = self.__copy)

        # Paste
        self.__thisEditMenu.add_command(label = "Paste", command = self.__paste)

        # Editing
        self.__thisMenuBar.add_cascade(label = "Edit", menu = self.__thisEditMenu)

        # Font: Arial
        self.__thisFontMenu.add_command(label = "Arial", command = self.__setArial)

        # Font: Comic Sans
        self.__thisFontMenu.add_command(label = "Comic Sans", command = self.__setComicSans)

        # Formatting
        self.__thisMenuBar.add_cascade(label = "Format", menu = self.__thisFormatMenu)

        # Fonts
        self.__thisFormatMenu.add_cascade(label = "Font", menu = self.__thisFontMenu)

        # Description
        self.__thisHelpMenu.add_command(label = "About Notepad", command = self.__showAbout)
        self.__thisMenuBar.add_cascade(label = "Help", menu = self.__thisHelpMenu)

        self.__root.config(menu = self.__thisMenuBar)

        self.__thisScrollBar.pack(side = RIGHT, fill = Y)

        # Scrollbar adjusts according to content
        self.__thisScrollBar.config(command = self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand = self.__thisScrollBar.set)

    def __quitApplication(self):
        self.__root.destroy()
        # exit()

    def __showAbout(self):
        showinfo("Notepad", "Mrinal Verma")
    
    def __openFile(self):
        self.__file = askopenfilename(defaultextension = ".txt",
            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

        if self.__file == "":
            # no file to open
            self.__file = None
        else:
            # try to open the file
            # set the window title
            self.__root.title(os.path.basename(self.__file) + " - Notepad")
            self.__thisTextArea.delete(1.0, END)
            
            file = open(self.__file, "r")

            self.__thisTextArea.insert(1.0, file.read())

            file.close()

    def __newFile(self):
        self.__root.title("Untitled -- Notepad")
        self.__file = None
        self.__thisTextArea.delete(1.0, END)

    def __saveFile(self):

        if self.__file == None:
            # save as new file
            self.__file = asksaveasfilename(initialfile='Untitled.txt',
                defaultextension=".txt",
                filetypes=[("All Files","*.*"),
                    ("Text Documents","*.txt")])

            if self.__file == "":
                self.__file = None
            else:
                # try to save the file
                file = open(self.__file, "w")
                file.write(self.__thisTextArea.get(1.0, END))
                file.close()
                # change the window title
                self.__root.title(os.path.basename(self.__file) + " - Notepad")

        else:
            file = open(self.__file, "w")
            file.write(self.__thisTextArea.get(1.0, END))
            file.close

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def __setArial(self):
        self.__thisTextArea.configure(font=("Arial", 10))

    def __setComicSans(self):
        self.__thisTextArea.configure(font=("Comic Sans MS", 10))

    def run(self):
        # Run main application
        self.__root.mainloop()

notepad = Notepad(width = 600, height = 600)
notepad.run()