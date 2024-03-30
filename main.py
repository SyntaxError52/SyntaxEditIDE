###SyntaxEdit
##Import Modules
from tkinter import *
from tkinter import filedialog, colorchooser, font
import tkinter as tk
import subprocess as sub
import sys as sy
  
##Graphical Configirations
win = tk.Tk()
win.title('SyntaxEdit')
win.iconbitmap(r'SyntaxEditLogo.ico')
win.configure(bg="black")
win.geometry("500x600")

title = tk.Label(win, text="SyntaxEdit", font=('Courier New', 25), bg='black', fg='white')
title.pack()

##Text Enter Location
entry = tk.Text(win, height=100, width=150, font=('Courier New', 12), bg='#212121', fg='#31bd62')
entry.pack()

##File Handaling
def appendToFile(event):
    userCode = entry.get("1.0", tk.END).strip()
    userFileLocation = filedialog.askopenfilename(title="Save to file")
    try:
        with open(userFileLocation, 'w') as file:
            file.write(userCode)
    except:
        pass

def openFile(event):
    userFileLocation = filedialog.askopenfilename(title="Open file")
    try:
        with open(userFileLocation, 'r') as file:
            userFileContent = file.read()
            entry.delete("1.0", tk.END)
            entry.insert(tk.END, userFileContent)
        win.title(f'SyntaxEdit - {userFileLocation}')
    except:
        pass

def newFile(event):
    userFileLocation = filedialog.askopenfilename(initialdir="C:\\Users",defaultextension='.txt',filetypes=[
        ("Text file",".txt"),
        ("HTML file", ".htm"),("JavaScript file", ".js"),("CSS file", ".css"),
        ("Python file", ".py"),
        ("C file", ".c"),("C# file", ".cs"),("C++ file", ".c++"),
        ("Java file", ".java"),("JSON file", ".json"),
        ("Lua file", ".lua"),
        ("R file", ".r"),
        ("Rust file", ".rs"),
        ("All files", ".*")], title="Create File")
    try:    
        with open(userFileLocation, 'w') as file:
            file.write('##//File Created with SyntaxEdit')
        openFile()
    except:
        pass
    
def runFile(event):
    userFileLocation = filedialog.askopenfilename(title="Select file to run")
    if sy.platform == "win32":
        command = ["cmd.exe", "/c", userFileLocation]
    else:
        command = ["sh", userFileLocation]
    try:
        sub.run(command)
    except:
        pass

def replaceText(event):
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

def findText(event):
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
        userCharHighlight = '<<<<<<' + userChar + '>>>>>>'
        newContent = entry.get("1.0", tk.END).strip().replace(userChar, userCharHighlight)
        entry.delete("1.0", tk.END)
        entry.insert("1.0", newContent)
    findButton = tk.Button(find, text='Find', command=findChar)
    findButton.pack()
    find.mainloop()

def clearFile(event):
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
    tk.Label(cl, font=('Courier New Bold', 25), fg='white', bg='black', text='v1.2').pack()
    tk.Label(cl, font=('Courier New', 15), fg='white', bg='black', text='Added Keyboard Shortcuts').pack()
    tk.Label(cl, font=('Courier New', 15), fg='white', bg='black', text='Added File Location Title').pack()
    tk.Label(cl, font=('Courier New', 15), fg='white', bg='black', text='Added Help').pack()
    tk.Label(cl, font=('Courier New Bold', 25), fg='white', bg='black', text='v1.3').pack()
    tk.Label(cl, font=('Courier New', 15), fg='white', bg='black', text='Added Templates').pack()
    cl.mainloop()


def help():
    hp = tk.Tk()
    hp.title('SyntaxEdit - Help')
    hp.iconbitmap(r'SyntaxEditLogo.ico')
    hp.configure(bg="black")
    hp.geometry("400x175")
    tk.Label(hp, font=('Courier New Bold', 25), fg='white', bg='black', text='Help Page').pack()
    tk.Label(hp, font=('Courier New', 15), fg='white', bg='black', text='Handle files using the file menu').pack()
    tk.Label(hp, font=('Courier New', 15), fg='white', bg='black', text='Check changes in the changelog').pack()
    tk.Label(hp, font=('Courier New', 15), fg='white', bg='black', text='Enter your code in the text box').pack()
    tk.Label(hp, font=('Courier New', 15), fg='white', bg='black', text='Github Repo Name: SyntaxEditIDE').pack()
    hp.mainloop()

def changeColor():
    color = colorchooser.askcolor(title='Pick a color')
    entry.config(fg=color[1])

def lightMode():
    win.config(bg='#C9C9C9')
    title.config(bg='#C9C9C9', fg='black')
    entry.config(bg='#EDEDED', fg='black')

def darkMode(event):
    win.config(bg='black')
    title.config(bg='black', fg='white')
    entry.config(bg='#212121', fg='white')

def privMode(event):
    win.config(bg='black')
    title.config(bg='black', fg='white')
    entry.config(fg='#212121', bg='#212121')

def changeFont():
    fontConfig = tk.Tk()
    fontConfig.title('SyntaxEdit - Font Configurations')
    fontConfig.iconbitmap(r'SyntaxEditLogo.ico')
    fontConfig.geometry('500x500')
    userFont = tk.StringVar(fontConfig, win)
    fontBox = tk.OptionMenu(fontConfig, userFont, *font.families())
    fontBox.pack()
    tk.Label(fontConfig, text='Font Size:').pack()
    sizeEntry = tk.Entry(fontConfig)
    sizeEntry.pack()
    def applyFont():
        try:
            entry.config(font=(userFont.get(), int(sizeEntry.get())))
        except ValueError:
            pass
    tk.Button(fontConfig, text='Apply', command=applyFont).pack()
    fontConfig.mainloop()

##Templates
def htmlTemp():
    entry.delete('0.0', tk.END)
    entry.insert('1.0','<!DOCTYPE html> \n')
    entry.insert('2.0', '<html lang="en"> \n')
    entry.insert('3.0', '<head> \n')
    entry.insert('4.0', '   <title>Webpage</title> \n')
    entry.insert('5.0', '   <link rel="stylesheet" href="styles.css"> \n')
    entry.insert('6.0', '   <script src="main.js"></script> \n')
    entry.insert('7.0', '</head> \n')
    entry.insert('8.0', '<body> \n')
    entry.insert('9.0', '   <p>HTML</p> \n')
    entry.insert('10.0', '</body> \n')
    entry.insert('11.0', '</html> \n')

def pyTempGUI():
    entry.delete('0.0', tk.END)
    entry.insert('1.0', 'from tkinter import * \n')
    entry.insert('2.0', '\n')
    entry.insert('3.0', 'root = Tk() \n')
    entry.insert('4.0', 'root.title("Python GUI using tkinter!") \n')
    entry.insert('5.0', 'root.iconbitmap(r"icon.ico") \n')
    entry.insert('6.0', 'root.geometry("500x500") \n')
    entry.insert('7.0', '\n')
    entry.insert('8.0', '\n')
    entry.insert('9.0', '\n')
    entry.insert('10.0', 'root.mainloop() \n')

##Menu Command
def appendToFileFM():
    appendToFile(Event)

def openFileFM():
    openFile(Event)

def newFileFM():
    newFile(Event)
    
def runFileFM():
    runFile(Event)

def replaceTextFM():
    replaceText(Event)

def findTextFM():
    findText(Event)

def clearFileFM():
    clearFile(Event)

def privModeFM():
    privMode(Event)

def darkModeFM():
    darkMode(Event)

##Keyboard Shortcuts
#File Handaling
win.bind('<Control-s>', appendToFile)
win.bind('<Control-o>', openFile)
win.bind('<Control-n>', newFile)
win.bind('<Control-r>', runFile)
#Other Bindings
win.bind('<Control-h>', replaceText)
win.bind('<Control-f>', findText)
win.bind('<Control-l>', clearFile)
win.bind('<Control-p>', privMode)
win.bind('<Control-0>', darkMode)
win.bind('<Control-slash>', quit)

##Menubar
menubar = Menu(win)
win.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File',menu=fileMenu)
fileMenu.add_command(label='Open',command=openFileFM)
fileMenu.add_command(label='New',command=newFileFM)
fileMenu.add_command(label='Save',command=appendToFileFM)
fileMenu.add_command(label='Run',command=runFileFM)
fileMenu.add_separator()
fileMenu.add_command(label='Exit',command=quit)

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit',menu=editMenu)
editMenu.add_command(label='Replace',command=replaceTextFM)
editMenu.add_command(label='Find',command=findTextFM)
editMenu.add_command(label='Clear',command=clearFileFM)

tempsMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Templates',menu=tempsMenu)
tempsMenu.add_command(label='Basic HTML',command=htmlTemp)
tempsMenu.add_command(label='Python GUI',command=pyTempGUI)

otherMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Other',menu=otherMenu)
otherMenu.add_command(label='Changelog',command=openChangelog)
otherMenu.add_command(label='Help',command=help)
otherMenu.add_separator()
otherMenu.add_command(label='Change Color',command=changeColor)
otherMenu.add_command(label='Change Font and Size',command=changeFont)
otherMenu.add_separator()
otherMenu.add_command(label='Light Mode',command=lightMode)
otherMenu.add_command(label='Dark Mode',command=darkModeFM)
otherMenu.add_command(label='Private Mode',command=privModeFM)

win.mainloop()
