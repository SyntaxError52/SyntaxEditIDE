###SyntaxEdit
##Import Modules
from tkinter import filedialog, font
from tkinter import *
import subprocess as sub
import sys as sy
  
##Graphical Configirations
win = Tk()
win.title('SyntaxEdit')
win.configure(bg="black")
win.geometry("500x600")

title = Label(win, text="SyntaxEdit", font=('Courier New', 25), bg='black', fg='white')
title.pack()

##Text Enter Location
entry = Text(win, height=100, width=150, font=('Courier New', 12), bg='#212121', fg='white')
entry.pack()

##File Handaling
def appendToFile(event=None):
    userCode = entry.get("1.0", END).strip()
    userFileLocation = filedialog.asksaveasfilename(title="Save to file")
    if userFileLocation:
        try:
            with open(userFileLocation, 'w', encoding='utf-8') as file:
                file.write(userCode)
        except Exception as e:
            print(f"Error writing to file: {e}")

def openFile(event=None):
    userFileLocation = filedialog.askopenfilename(title="Open file")
    if userFileLocation:
        try:
            with open(userFileLocation, 'r', encoding='utf-8') as file:
                userFileContent = file.read()
                entry.delete("1.0", "end")
                entry.insert("end", userFileContent)
            win.title(f'SyntaxEdit - {userFileLocation}')
        except Exception as e:
            print(f"Error opening file: {e}")

def runFile(event=None):
    userFileLocation = filedialog.askopenfilename(title="Select file to run")
    if userFileLocation:
        try:
            if sy.platform == "win32":
                command = [sy.executable, userFileLocation]
            else:
                command = [sy.executable, userFileLocation]

            sub.run(command, shell=True)
        except Exception:
            pass

def replaceText(event):
    replace = Tk()
    replace.title('SyntaxEdit - Replace')
    findEntryLabel = Label(replace, text='Find: ', width=100)
    findEntryLabel.pack()
    find = Entry(replace, width=30)
    find.pack()
    replaceEntryLabel = Label(replace, text='Replace: ', width=100)
    replaceEntryLabel.pack()
    replaceE = Entry(replace, width=30)
    replaceE.pack()
    def getCharValues():
        userChar1 = find.get().strip()
        userChar2 = replaceE.get().strip()
        newContent = entry.get("1.0", END).strip().replace(userChar1, userChar2)
        entry.delete("1.0", END)
        entry.insert("1.0", newContent)
    replaceButton = Button(replace, text='Replace', command=getCharValues)
    replaceButton.pack()
    replace.mainloop()

def findText(event):
    find = Tk()
    find.title('SyntaxEdit - Find')
    findEntryLabel = Label(find, text='Find: ', width=100)
    findEntryLabel.pack()
    findBox = Entry(find, width=30)
    findBox.pack()
    def findChar():
        userChar = findBox.get()
        userWanted = entry.get("1.0", END).strip().find(userChar)
        userCharHighlight = '<<<<<<' + userChar + '>>>>>>'
        newContent = entry.get("1.0", END).strip().replace(userChar, userCharHighlight)
        entry.delete("1.0", END)
        entry.insert("1.0", newContent)
    findButton = Button(find, text='Find', command=findChar)
    findButton.pack()
    find.mainloop()

def clearFile(event):
    warning = Tk()
    warning.title('SyntaxEdit - Find')
    Label(warning, text='Are you sure you want to clear the content of this file', width=100).pack()
    def clearCont():
        entry.delete("1.0", END)
    Button(warning, text='Clear File', command=clearCont).pack()
    warning.mainloop()

def help():
    hp = Tk()
    hp.title('SyntaxEdit - Help')
    hp.configure(bg="black")
    hp.geometry("400x175")
    Label(hp, font=('Courier New Bold', 25), fg='white', bg='black', text='Help Page').pack()
    Label(hp, font=('Courier New', 15), fg='white', bg='black', text='Handle files using the file menu').pack()
    Label(hp, font=('Courier New', 15), fg='white', bg='black', text='Enter your code in the text box').pack()
    Label(hp, font=('Courier New', 15), fg='white', bg='black', text='Add Syntax Highlight by selecting language').pack()
    Label(hp, font=('Courier New', 15), fg='white', bg='black', text='Github Repo Name: SyntaxEditIDE').pack()
    hp.mainloop()

def lightMode():
    win.config(bg='#C9C9C9')
    title.config(bg='#C9C9C9', fg='black')
    entry.config(bg='#EDEDED', fg='black')

def darkMode(event):
    win.config(bg='black')
    title.config(bg='black', fg='white')
    entry.config(bg='#212121', fg='white')

def changeFont():
    fontConfig = Tk()
    fontConfig.title('SyntaxEdit - Font Configurations')
    fontConfig.geometry('500x500')
    userFont = StringVar(fontConfig, win)
    fontBox = OptionMenu(fontConfig, userFont, *font.families())
    fontBox.pack()
    Label(fontConfig, text='Font Size:').pack()
    sizeEntry = Entry(fontConfig)
    sizeEntry.pack()
    def applyFont():
        try:
            entry.config(font=(userFont.get(), int(sizeEntry.get())))
        except ValueError:
            pass
    Button(fontConfig, text='Apply', command=applyFont).pack()
    fontConfig.mainloop()

##Templates
def htmlTemp():
    entry.delete('0.0', END)
    entry.insert('1.0', '''
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Webpage</title>
    <link rel="stylesheet" href="______.css">
    <script src="____.js"></script>
</head>
<body>
    <p>Hello, World</p>
    <div class="watermark">Made with Syntax Edit</div>
</body>
</html>
''')

def pyTempGUI():
    entry.delete('0.0', END)
    entry.insert('1.0', '''
from tkinter import *
                 
root = Tk()
root.title('Tkinter GUI')
root.geometry('420x420')
                 
root.mainloop()  
''')

##Menu Command
def appendToFileFM():
    appendToFile(Event)

def openFileFM():
    openFile(Event)
    
def runFileFM():
    runFile(Event)

def replaceTextFM():
    replaceText(Event)

def findTextFM():
    findText(Event)

def clearFileFM():
    clearFile(Event)

def darkModeFM():
    darkMode(Event)


##Syntax Highlighting
    
entry.tag_configure('default', foreground='white')

def assign_color(word, color):
    entry.tag_configure(color, foreground=color)
    start = '1.0'
    while True:
        start = entry.search(word, start, END)
        if not start:
            break
        end = entry.index(f'{start}+{len(word)}c')
        entry.tag_add(color, start, end)
        start = end

def setLang(lang):
    if lang == 'py':
        def on_key(event):
            entry.tag_configure('default', foreground='white')
            assign_color('#', 'green')
            assign_color('import', '#738dbd')
            assign_color('from', '#738dbd')
            assign_color('*', '#738dbd')
            assign_color('while', 'purple')
            assign_color('for', 'purple')
            assign_color('item', 'yellow')
            assign_color('def', '#738dbd')
            assign_color('if', 'purple')
            assign_color('else', 'purple')
            assign_color('elif', 'purple')
            assign_color('\'', 'green')
            assign_color('\"', 'green')
            assign_color('=', 'yellow')
            assign_color(':', 'yellow')
            assign_color(',', 'yellow')
            assign_color('.', 'yellow')
            assign_color('pass', 'purple')
            assign_color('True', 'green')
            assign_color('False', 'green')
            assign_color(';', 'red')
    elif lang == 'html':
        def on_key(event):
            entry.tag_configure('default', foreground='white')
            assign_color('<', 'green')
            assign_color('>', 'green')
            assign_color('/', 'purple')
            assign_color('\'', 'green')
            assign_color('\"', 'green')
            assign_color('=', 'yellow')
            assign_color('div', '#738dbd')
            assign_color('span', '#738dbd')
            assign_color('src', '#738dbd')
            assign_color('href', '#738dbd')
            assign_color('rel', '#738dbd')
            assign_color('type', '#738dbd')
            assign_color('class', '#738dbd')
            assign_color('id', '#738dbd')
    elif lang == 'css':
        def on_key(event):
            entry.tag_configure('default', foreground='white')
            assign_color('.', 'yellow')
            assign_color('#', 'yellow')
            assign_color('body', 'yellow')
            assign_color('"', 'green')
            assign_color('\'', 'green')
            assign_color('/*', 'green')
            assign_color('{', 'yellow')
            assign_color('}', 'yellow')
            assign_color(':', 'yellow')
    elif lang == 'js':
        def on_key(event):
            entry.tag_configure('default', foreground='white')
            assign_color('.', 'yellow')
            assign_color('=', 'yellow')
            assign_color('let', '#738dbd')
            assign_color('var', '#738dbd')
            assign_color('"', 'green')
            assign_color('\'', 'green')
            assign_color('/', 'green')
            assign_color('{', 'yellow')
            assign_color('}', 'yellow')
            assign_color(';', 'yellow')

    win.bind('<Key>', on_key)


##Keyboard Shortcuts
#File Handaling
win.bind('<Control-s>', appendToFile)
win.bind('<Control-o>', openFile)
win.bind('<Control-r>', runFile)
#Other Bindings
win.bind('<Control-h>', replaceText)
win.bind('<Control-f>', findText)
win.bind('<Control-l>', clearFile)
win.bind('<Control-0>', darkMode)
win.bind('<Control-slash>', quit)

##Menubar
menubar = Menu(win)
win.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File',menu=fileMenu)
fileMenu.add_command(label='Open',command=openFileFM)
fileMenu.add_command(label='Save',command=appendToFileFM)
fileMenu.add_command(label='Run',command=runFileFM)
fileMenu.add_separator()
fileMenu.add_command(label='Exit',command=quit)

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit',menu=editMenu)
editMenu.add_command(label='Replace',command=replaceTextFM)
editMenu.add_command(label='Find',command=findTextFM)
editMenu.add_command(label='Clear',command=clearFileFM)

langMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Language',menu=langMenu)
langMenu.add_command(label='Python', command=lambda: setLang('py'))
langMenu.add_command(label='HTML', command=lambda: setLang('html'))
langMenu.add_command(label='CSS', command=lambda: setLang('css'))
langMenu.add_command(label='JS', command=lambda: setLang('js'))

tempsMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Templates',menu=tempsMenu)
tempsMenu.add_command(label='Basic HTML',command=htmlTemp)
tempsMenu.add_command(label='Python GUI',command=pyTempGUI)

otherMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Other',menu=otherMenu)
otherMenu.add_command(label='Help',command=help)
otherMenu.add_separator()
otherMenu.add_command(label='Change Font and Size',command=changeFont)
otherMenu.add_separator()
otherMenu.add_command(label='Light Mode',command=lightMode)
otherMenu.add_command(label='Dark Mode',command=darkModeFM)

win.mainloop()
