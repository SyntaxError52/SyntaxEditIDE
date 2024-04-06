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

##Text Enter Location
entry = Text(win, height=28, width=150, font=('Courier New', 12), bg='#212121', fg='white')
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
    findEntryLabel = Label(win, text='Find: ', width=100, fg='white', bg='black')
    findEntryLabel.pack()
    find = Entry(win, width=30, fg='white', bg='#212121')
    find.pack()
    replaceEntryLabel = Label(win, text='Replace: ', width=100, fg='white', bg='black')
    replaceEntryLabel.pack()
    replace = Entry(win, width=30, fg='white', bg='#212121')
    replace.pack()
    def getCharValues():
        userChar1 = find.get().strip()
        userChar2 = replace.get().strip()
        newContent = entry.get("1.0", END).strip().replace(userChar1, userChar2)
        entry.delete("1.0", END)
        entry.insert("1.0", newContent)
        findEntryLabel.destroy()
        find.destroy()
        replaceEntryLabel.destroy()
        replace.destroy()
        replaceButton.destroy()
    replaceButton = Button(win, text='Replace', command=getCharValues, fg='white', bg='#212121')
    replaceButton.pack()
    replace.mainloop()

def findText(event):
    findEntryLabel = Label(win, text='Find: ', width=100, fg='white', bg='black')
    findEntryLabel.pack()
    findBox = Entry(win, width=30, fg='white', bg='#212121')
    findBox.pack()
    def findChar():
        userChar = findBox.get()
        userWanted = entry.get("1.0", END).strip().find(userChar)
        userCharHighlight = '<<<<<<' + userChar + '>>>>>>'
        newContent = entry.get("1.0", END).strip().replace(userChar, userCharHighlight)
        entry.delete("1.0", END)
        entry.insert("1.0", newContent)
        findEntryLabel.destroy()
        findBox.destroy()
        findButton.destroy()
    findButton = Button(win, text='Find', command=findChar, fg='white', bg='#212121')
    findButton.pack()
    find.mainloop()

def clearFile(event):
    warning = Label(win, text='Are you sure you want to clear the content of this file', width=100, fg='white', bg='black')
    warning.pack()
    def clearCont():
        entry.delete("1.0", END)
        warning.destroy()
        okay.destroy()
    okay =  Button(win, text='Clear File', command=clearCont, fg='white', bg='#212121')
    okay.pack()
    warning.mainloop()

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
win.bind('<Control-slash>', quit)

##Menubar
menubar = Menu(win)
win.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File',menu=fileMenu)
fileMenu.add_command(label='Open',command=lambda: openFile(None))
fileMenu.add_command(label='Save',command=lambda: appendToFile(None))
fileMenu.add_command(label='Run',command=lambda: runFile(None))
fileMenu.add_separator()
fileMenu.add_command(label='Exit',command=quit)

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit',menu=editMenu)
editMenu.add_command(label='Replace',command=lambda: replaceText(None))
editMenu.add_command(label='Find',command=lambda: findText(None))
editMenu.add_command(label='Clear',command=lambda: clearFile(None))

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

win.mainloop()
