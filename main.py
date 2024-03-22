###SyntaxEdit
##Import Modules
from tkinter import *
from tkinter import filedialog, colorchooser
import tkinter as tk
import subprocess as sub
import sys as sy
  
##Graphical Configirations
win = tk.Tk()
win.title("SyntaxEdit")
win.iconbitmap(r'SyntaxEditLogo.ico')
win.configure(bg="black")
win.geometry("500x600")

title = tk.Label(win, text="SyntaxEdit", font=('Courier New', 25), bg='black', fg='white')
title.pack()

##Text Enter Location
entry = tk.Text(win, height=100, width=150, font=('Courier New', 12), bg='#212121', fg='#31bd62')
entry.pack()

##File Handaling
def appendToFile():
    userCode = entry.get("1.0", tk.END).strip()
    userFileLocation = filedialog.askopenfilename(title="Save to file")
    with open(userFileLocation, 'w') as file:
        file.write(userCode)

def openFile():
    userFileLocation = filedialog.askopenfilename(title="Open file")
    with open(userFileLocation, 'r') as file:
        userFileContent = file.read()
        entry.delete("1.0", tk.END)
        entry.insert(tk.END, userFileContent)

def newFile():
    userFileLocation = filedialog.asksaveasfile(initialdir="C:\\Users",defaultextension='.txt',filetypes=[
        ("Text file",".txt"),
        ("HTML file", ".htm"),("JavaScript file", ".js"),("CSS file", ".css"),
        ("Python file", ".py"),
        ("C file", ".c"),("C# file", ".cs"),("C++ file", ".c++"),
        ("Java file", ".java"),("JSON file", ".json"),
        ("Lua file", ".lua"),
        ("R file", ".r"),
        ("Rust file", ".rs"),
        ("All files", ".*")], title="Create File")
    with open(userFileLocation, 'w') as file:
        file.write('##//File Created with SyntaxEdit')
    openFile()
    
def runFile():
    userFileLocation = filedialog.askopenfilename(title="Select file to run")
    if sy.platform == "win32":
        command = ["cmd.exe", "/c", userFileLocation]
    else:
        command = ["sh", userFileLocation]
    sub.run(command)

def replaceText():
    replace = tk.Tk()
    replace.title('SyntaxEdit - Replace')
    replace.iconbitmap(r'SyntaxEditLogo.ico')
    findEntryLabel = tk.Label(replace, text='Find: ', width=100)
    findEntryLabel.pack()
    find = tk.Entry(replace, width=30)
    find.pack()
    replaceEntryLabel = tk.Label(replace, text='Replace: ', width=100)
    replaceEntryLabel.pack()
    replaceE = tk.Entry(replace, width=30)
    replaceE.pack()
    def getCharValues():
        userChar1 = find.get().strip()
        userChar2 = replaceE.get().strip()
        newContent = entry.get("1.0", tk.END).strip().replace(userChar1, userChar2)
        entry.delete("1.0", tk.END)
        entry.insert("1.0", newContent)
    replaceButton = tk.Button(replace, text='Replace', command=getCharValues)
    replaceButton.pack()
    replace.mainloop()

def findText():
    find = tk.Tk()
    find.title('SyntaxEdit - Find')
    find.iconbitmap(r'SyntaxEditLogo.ico')
    findEntryLabel = tk.Label(find, text='Find: ', width=100)
    findEntryLabel.pack()
    findBox = tk.Entry(find, width=30)
    findBox.pack()
    def findChar():
        userChar = findBox.get()
        userWanted = entry.get("1.0", tk.END).strip().find(userChar)
        userCharHighlight = '<<<<<' + userChar + '>>>>>'
        newContent = entry.get("1.0", tk.END).strip().replace(userChar, userCharHighlight)
        entry.delete("1.0", tk.END)
        entry.insert("1.0", newContent)
    findButton = tk.Button(find, text='Find', command=findChar)
    findButton.pack()
    find.mainloop()

def clearFile():
    warning = tk.Tk()
    warning.title('SyntaxEdit - Find')
    warning.iconbitmap(r'SyntaxEditLogo.ico')
    tk.Label(warning, text='Are you sure you want to clear the content of this file', width=100).pack()
    def clearCont():
        entry.delete("1.0", tk.END)
    tk.Button(warning, text='Clear File', command=clearCont).pack()
    warning.mainloop()

def openChangelog():
    cl = tk.Tk()
    cl.title('SyntaxEdit - Changelog')
    cl.iconbitmap(r'SyntaxEditLogo.ico')
    cl.configure(bg="black")
    cl.geometry("400x500")
    tk.Label(cl, font=('Courier New Bold', 25), fg='white', bg='black', text='v1.0').pack()
    tk.Label(cl, font=('Courier New', 15), fg='white', bg='black', text='Added Editor').pack()
    tk.Label(cl, font=('Courier New', 15), fg='white', bg='black', text='Added Dropdown Menu').pack()
    tk.Label(cl, font=('Courier New', 15), fg='white', bg='black', text='Added Find and Replace').pack()
    tk.Label(cl, font=('Courier New', 15), fg='white', bg='black', text='Added Find').pack()
    tk.Label(cl, font=('Courier New', 15), fg='white', bg='black', text='Added Dark Mode').pack()
    tk.Label(cl, font=('Courier New', 15), fg='white', bg='black', text='Added Clear Code').pack()
    tk.Label(cl, font=('Courier New Bold', 25), fg='white', bg='black', text='v1.1').pack()
    tk.Label(cl, font=('Courier New', 15), fg='white', bg='black', text='Added Light Mode').pack()
    tk.Label(cl, font=('Courier New', 15), fg='white', bg='black', text='Added Chanage Color').pack()
    tk.Label(cl, font=('Courier New', 15), fg='white', bg='black', text='Added Font/Size').pack()
    tk.Label(cl, font=('Courier New', 15), fg='white', bg='black', text='Added Private Mode').pack()
    cl.mainloop()

def changeColor():
    color = colorchooser.askcolor(title='Pick a color')
    entry.config(fg=color[1])

def lightMode():
    win.config(bg='white')
    title.config(bg='white', fg='black')
    entry.config(bg='white')

def darkMode():
    win.config(bg='black')
    title.config(bg='black', fg='white')
    entry.config(bg='#212121')

def privMode():
    win.config(bg='black')
    title.config(bg='black', fg='white')
    entry.config(fg='#171717', bg='#212121')

def changeFont():
    fontConfig = tk.Tk()
    fontConfig.title('SyntaxEdit - Font Configurations')
    fontConfig.iconbitmap(r'SyntaxEditLogo.ico')
    fontConfig.geometry('500x500')
    tk.Label(fontConfig, text='Font Name:').pack()
    fontNameEntry = tk.Entry(fontConfig)
    fontNameEntry.pack()
    tk.Label(fontConfig, text='Font Size:').pack()
    sizeEntry = tk.Entry(fontConfig)
    sizeEntry.pack()
    def applyFont():
        entry.config(font=(fontNameEntry.get(), sizeEntry.get()))
    tk.Button(fontConfig, text='Apply', command=applyFont).pack()
    fontConfig.mainloop()

##Menubar
menubar = Menu(win)
win.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File',menu=fileMenu)
fileMenu.add_command(label='Open',command=openFile)
fileMenu.add_command(label='New',command=newFile)
fileMenu.add_command(label='Save',command=appendToFile)
fileMenu.add_command(label='Run',command=runFile)
fileMenu.add_separator()
fileMenu.add_command(label='Exit',command=quit)

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit',menu=editMenu)
editMenu.add_command(label='Replace',command=replaceText)
editMenu.add_command(label='Find',command=findText)
editMenu.add_command(label='Clear',command=clearFile)

otherMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Other',menu=otherMenu)
otherMenu.add_command(label='Changelog',command=openChangelog)
otherMenu.add_separator()
otherMenu.add_command(label='Change Color',command=changeColor)
otherMenu.add_command(label='Change Font and Size',command=changeFont)
otherMenu.add_separator()
otherMenu.add_command(label='Light Mode',command=lightMode)
otherMenu.add_command(label='Dark Mode',command=darkMode)
otherMenu.add_command(label='Private Mode',command=privMode)

win.mainloop()
