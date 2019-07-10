# NOTES

## Telegram Informations

- My chat Id : 648853802
- Jhenifer's chat ID : x

```python
def sendMsg():
    r = requests.get("https://api.telegram.org/bot848233233:AAFKYXkCxGgjZ6b32dPbkqE023uh1Ga-R94/sendMessage?chat_id=648853802&text=Hello%20World")
```

## Default VSCODE Settings

- Install pep8 and autopep8 from pip

- CTRL+SHIFT+P > Linting | Format Doc

- Used Extesions
  - ayu
  - Code Runner
  - HTML Preview
  - markdownlint
  - Material Icon Theme
  - Night Owl
  - Noctis
  - Python
  - vscode-icons
  - Winter is Coming Theme

- VSCODE Settings JSON File

```json
{
    "window.zoomLevel": 0,
    "terminal.integrated.shell.windows": "C:\\WINDOWS\\System32\\cmd.exe",
    "workbench.colorTheme": "Ayu Mirage Bordered",
    "workbench.iconTheme": "material-icon-theme",
    "git.autofetch": true,
    "workbench.sideBar.location": "left",
    "workbench.settings.editor": "json",
    "workbench.startupEditor": "newUntitledFile",
    "editor.fontSize": 14, //default 14,
    "editor.fontWeight": "500",
    // "editor.fontFamily": ..,
    "debug.console.fontSize": 14,
    // "debug.console.fontFamily": ..,
    "terminal.integrated.fontSize": 14,
    // "terminal.integrated.fontFamily": 14,
    "python.formatting.provider": "autopep8",
    "editor.formatOnSave": true,
    "python.pythonPath": "python", // your path here
    "code-runner.executorMap": {
        "javascript": "node",
        "java": "cd $dir && javac $fileName && java $fileNameWithoutExt",
        "c": "cd $dir && gcc $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
        "cpp": "cd $dir && g++ $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
        "objective-c": "cd $dir && gcc -framework Cocoa $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
        "php": "php",
        "python": "$pythonPath -u",
        "perl": "perl",
        "perl6": "perl6",
        "ruby": "ruby",
        "go": "go run",
        "lua": "lua",
        "groovy": "groovy",
        "powershell": "powershell -ExecutionPolicy ByPass -File",
        "bat": "cmd /c",
        "shellscript": "bash",
        "fsharp": "fsi",
        "csharp": "scriptcs",
        "vbscript": "cscript //Nologo",
        "typescript": "ts-node",
        "coffeescript": "coffee",
        "scala": "scala",
        "swift": "swift",
        "julia": "julia",
        "crystal": "crystal",
        "ocaml": "ocaml",
        "r": "Rscript",
        "applescript": "osascript",
        "clojure": "lein exec",
        "haxe": "haxe --cwd $dirWithoutTrailingSlash --run $fileNameWithoutExt",
        "rust": "cd $dir && rustc $fileName && $dir$fileNameWithoutExt",
        "racket": "racket",
        "ahk": "autohotkey",
        "autoit": "autoit3",
        "dart": "dart",
        "pascal": "cd $dir && fpc $fileName && $dir$fileNameWithoutExt",
        "d": "cd $dir && dmd $fileName && $dir$fileNameWithoutExt",
        "haskell": "runhaskell",
        "nim": "nim compile --verbosity:0 --hints:off --run",
        "lisp": "sbcl --script",
        "kit": "kitc --run",
        "code-runner.clearPreviousOutput": false,
        "code-runner.showExecutionMessage": true
    }
}
```

## Database Services

- Host: www.freemysqlhosting.net - Site : phpmyadmin.co - 5MB Free
- Host: remotemysql.com - Site : remotemysql.com/phpmyadmin - 100MB Free

## Task schedual (Tkinter)

```python
from tkinter import *
h1, h2 = "HELLO", "WORLD"

def do_something():
    global h1, h2
    root.title(h1)
    h1, h2 = h2, h1
    root.after(2000, do_something)
```

```python
# or can use time.sleep(2) instead
import threading

def hello():
    print("hello, world")

t = threading.Timer(2.0, hello) # 2 seconds
t.cancel() # only if the timer didn't start yet

t.start()
```

## Passing functions with args in Tkinter

```python
from functools import partial

def change_label_number(num):
    pass

# didn't understand it very well
buttonExample = tk.Button(app, text="Increase", width=30,
                          command=partial(change_label_number, 2))
```

## JSON

Convert JSON to Dictionary: json.loads(x)

```python
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
```

Convert Dictinary to JSON: json.dumps(x, indent=4, separators=(". ", " = "), sort_keys=True)

```python
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
```

## Files

Sending "r" means open in read mode, which is the default.
Sending "w" means write mode, for rewriting the contents of a file. Rewriting only when: open("BearBot.json", "w") is called
Sending "a" means append mode, for adding new content to the end of the file.
Adding "b" to a mode opens it in binary mode, which is used for non-text files (such as image and sound files).

print(file.read(16)) - prints the first 16 caracters(bytes)
print(file.read()) - returns the rest of the file.
NB : if you read all the content.. Attempting to read more without output an empty string.

To retrieve each line in a file, you can use the readlines method to return a list in which each element is a line in the file.
file.readlines()

```python
# Method 1
with open("BearBot.json", "w") as file:
    file.write("Hello World")

# Method 2
file = open("BearBot.json", "r")
cont = file.read()
print(cont)
file.close()

# Method 3
try:
   f = open("filename.txt", "a")
   print(f.write("New text"))
finally:
   f.close()
```

## Decorators

```python
def decor(func):
    def wrap(*args, **kwargs):
        print("---- START OF FUNC ----")
        func(*args, **kwargs)
        print("----- END OF FUNC -----")
    return wrap


@decor
def sayHello(name):
    print(f"Hello, {name}!")


sayHello("World")

```

## Modules: requests, bs4

pip install requests, bs4
pip install lxml, html5lib

```python
html_doc = """<!-- html code here -->"""
soup = BeautifulSoup(html_doc, "lxml")  # can use "lxml" or "html5lib"

with open("text.html", "w") as f:
    f.write(soup.prettify())
```
