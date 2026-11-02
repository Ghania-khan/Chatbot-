import tkinter as tk
from tkinter import font as tkfont
import random
import datetime
import threading
import time

try:
    import wikipedia
except ImportError:
    wikipedia = None

# PYTHON-INSPIRED COLOUR PALETTE 
BG_MAIN       = "#1e1e2e"   # deep dark navy (Python dark bg)
BG_PANEL      = "#2a2a3e"   # slightly lighter panel
BG_BUBBLE_U   = "#2b4f72"   # user bubble — Python blue tint
BG_BUBBLE_B   = "#2d4a1e"   # bot bubble — Python green tint
ACCENT_BLUE   = "#4b8bbe"   # Python official blue
ACCENT_YELLOW = "#ffd343"   # Python official yellow
ACCENT_GREEN  = "#6abf69"   # soft green for bot
ACCENT_PINK   = "#ff6b6b"   # error/badge red
ACCENT_GOLD   = "#ffd343"   # amber = same as yellow
ACCENT_PURPLE = "#c792ea"   # violet accent
TEXT_DARK     = "#e8eaf6"   # near-white for dark bg
TEXT_MID      = "#b0bec5"   # muted light grey
TEXT_DIM      = "#607d8b"   # dimmed timestamps
BORDER        = "#3a3a5c"   # dark border
ENTRY_BG      = "#252535"   # dark input bg
SHADOW        = "#16162a"   # deeper shadow

#   KNOWLEDGE BASE

knowledge = {

    # ── COMPUTER BASICS 

    "what is a computer": (
        "💻 WHAT IS A COMPUTER?\n\n"
        "A computer is basically a very fast, very obedient, but VERY literal machine.\n"
        "It does EXACTLY what you tell it — which is terrifying when you're a beginner 😅\n\n"
        "It has 4 main jobs:\n"
        "  📥 INPUT   — take data in (keyboard, mouse, mic)\n"
        "  🧠 PROCESS  — do stuff with it (CPU's job)\n"
        "  📤 OUTPUT  — show results (screen, printer, speaker)\n"
        "  💾 STORAGE  — remember things (RAM = short term, HDD/SSD = long term)\n\n"
        "Think of it like a very fast chef 👨‍🍳:\n"
        "  Ingredients = input → Kitchen = processor → Dish = output → Fridge = storage"
    ),

    "hardware": (
        "🔩 HARDWARE — the physical parts you can touch (and accidentally drop)\n\n"
        "Key components:\n\n"
        "  🧠 CPU (Central Processing Unit)\n"
        "     The brain of the computer. Executes instructions.\n"
        "     Measured in GHz — more = faster thinking.\n\n"
        "  🎮 RAM (Random Access Memory)\n"
        "     Short-term memory. Fast but forgets EVERYTHING when power cuts.\n"
        "     Like a whiteboard — great for working, bad for keeping.\n\n"
        "  💾 HDD / SSD (Hard/Solid State Drive)\n"
        "     Long-term storage. SSDs are much faster than HDDs.\n"
        "     Like a notebook — slower to read/write but keeps data forever.\n\n"
        "  🖥️ GPU (Graphics Processing Unit)\n"
        "     Renders visuals. Also used in AI/ML these days.\n"
        "     The overachiever that does millions of tiny tasks in parallel.\n\n"
        "  🔌 Motherboard\n"
        "     Connects EVERYTHING together. The city grid of your computer."
    ),

    "software": (
        "💿 SOFTWARE — the instructions that tell hardware what to do.\n\n"
        "Hardware without software = a very expensive paperweight 📦\n\n"
        "Two main types:\n\n"
        "  🏗️ SYSTEM SOFTWARE\n"
        "     → Operating System (Windows, macOS, Linux)\n"
        "     → Manages hardware, runs programs, handles files\n"
        "     → The landlord of your computer 🏠\n\n"
        "  📱 APPLICATION SOFTWARE\n"
        "     → Programs users actually use: Chrome, Word, Spotify, games\n"
        "     → Built ON TOP of the OS\n"
        "     → The tenants in the landlord's building 🏢\n\n"
        "Fun fact: Python code you write is application software!\n"
        "You're building the future, one bug at a time 🐛→🦋"
    ),

    "operating system": (
        "🖥️ OPERATING SYSTEM (OS) — the manager of your computer's chaos.\n\n"
        "Without an OS, programs couldn't talk to hardware at all.\n"
        "It's the translator between 'human stuff' and 'machine stuff'.\n\n"
        "What an OS does:\n"
        "  📁 Manages files and folders\n"
        "  🔄 Handles multitasking (runs many programs at once)\n"
        "  🔒 Controls security and user accounts\n"
        "  🔌 Talks to hardware drivers\n"
        "  📡 Manages networking\n\n"
        "Popular OSes:\n"
        "  🪟 Windows  — most popular for desktops\n"
        "  🍎 macOS    — for Apple fans with strong opinions\n"
        "  🐧 Linux    — for developers who enjoy suffering (lovingly)\n"
        "  📱 Android/iOS — mobile operating systems\n\n"
        "Python runs on ALL of them. True neutral ground! 🕊️"
    ),

    "binary": (
        "🔢 BINARY — the language computers ACTUALLY speak.\n\n"
        "Computers only understand TWO things: ON (1) and OFF (0).\n"
        "Everything — images, music, text, videos — is secretly just 0s and 1s.\n\n"
        "Why binary? Because transistors (tiny switches) are either ON or OFF.\n"
        "Simple, reliable, and computers can do BILLIONS of them per second 🚀\n\n"
        "Decimal → Binary examples:\n"
        "  0  →  0000\n"
        "  1  →  0001\n"
        "  2  →  0010\n"
        "  5  →  0101\n"
        "  10 →  1010\n\n"
        "Units of data:\n"
        "  1 bit      = 1 binary digit (0 or 1)\n"
        "  8 bits     = 1 byte (stores 1 character)\n"
        "  1024 bytes = 1 Kilobyte (KB)\n"
        "  1024 KB    = 1 Megabyte (MB)\n"
        "  1024 MB    = 1 Gigabyte (GB)\n\n"
        "So when your code has ONE character extra... it's literally 8 bits of chaos 😂"
    ),

    "internet": (
        "🌐 THE INTERNET — the world's biggest, messiest, most incredible network.\n\n"
        "The internet is a GLOBAL NETWORK of computers all talking to each other.\n"
        "Not one central place — just millions of devices all connected.\n\n"
        "Key concepts:\n\n"
        "  📡 IP Address — your computer's postal address on the internet\n"
        "     Example: 192.168.1.1 (IPv4) or the much longer IPv6\n\n"
        "  🌍 DNS — Domain Name System\n"
        "     Translates 'google.com' into a real IP address.\n"
        "     Like a phone book for the internet 📖\n\n"
        "  🤝 HTTP/HTTPS — how browsers and servers talk to each other\n"
        "     HTTPS = secure (the little 🔒 padlock in your browser)\n\n"
        "  ☁️ The Cloud — just someone else's computer (and that's okay)\n\n"
        "Fun fact: Python is HEAVILY used in web servers that power the internet!\n"
        "You're not just learning a language — you're learning to build the web 🌐"
    ),

    #  WHAT IS PYTHON 

    "what is python": (
        "🐍 WHAT IS PYTHON?\n\n"
        "Python is a high-level, general-purpose programming language created by\n"
        "Guido van Rossum in 1991. He named it after Monty Python 🎭\n"
        "(Yes, the comedy troupe. Programmers are funnier than you think.)\n\n"
        "Why Python is AMAZING:\n"
        "  Reads almost like plain English — very beginner friendly\n"
        "  Massive community — someone already solved your problem\n"
        "  Huge library ecosystem (pip install anything)\n"
        "  Used EVERYWHERE: web, AI, data science, automation, scripting\n\n"
        "Where Python is used:\n"
        "  🤖 Artificial Intelligence & Machine Learning\n"
        "  🌐 Web Development (Django, Flask, FastAPI)\n"
        "  📊 Data Science & Analytics (pandas, numpy)\n"
        "  🔧 Automation & Scripting\n"
        "  🎮 Game development (Pygame)\n"
        "  🔬 Scientific research\n\n"
        "Companies using Python: Google, Netflix, Instagram, NASA, Spotify 🚀\n\n"
        "Ask me: variable, list, function, loop, class, or any Python topic!"
    ),

    "python history": (
        "📜 PYTHON HISTORY — a brief, entertaining timeline\n\n"
        "  1989 → Guido van Rossum starts writing Python over Christmas holidays\n"
        "         (Because normal people bake cookies. Guido writes languages.) 🎄\n\n"
        "  1991 → Python 0.9.0 released. The world didn't know yet.\n\n"
        "  2000 → Python 2.0 — list comprehensions, garbage collection! 🎉\n\n"
        "  2008 → Python 3.0 released — broke backward compatibility.\n"
        "         The programming community: 😱😡🤯 (still recovering)\n\n"
        "  2010 → Python 2 and 3 co-exist awkwardly, like exes at a party.\n\n"
        "  2020 → Python 2 officially retired. RIP. Gone but not forgotten.\n\n"
        "  Today → Python is the #1 most popular programming language 🏆\n"
        "           Used by over 8 million developers worldwide!\n\n"
        "Moral: Good things take time... and maybe a boring Christmas 🎅"
    ),

    # ── PROGRAMMING FUNDAMENTALS ─────────────────────────────────────────────

    "variable": (
        "📦 VARIABLES — labelled boxes for storing data.\n\n"
        "You give data a name so you can use it later.\n"
        "Like labelling your containers in the fridge (which you don't do, admit it) 🧊\n\n"
        "```python\n"
        "age      = 25          # integer — whole number\n"
        "name     = 'Alex'      # string  — text\n"
        "height   = 5.9         # float   — decimal number\n"
        "is_cool  = True        # boolean — True or False\n"
        "\n"
        "print(name, 'is', age, 'years old')\n"
        "# Output: Alex is 25 years old\n"
        "```\n\n"
        "Naming rules:\n"
        "  ✅ use_underscores_like_this  (snake_case)\n"
        "  ✅ meaningful names: user_age NOT x47\n"
        "  ❌ cannot start with a number: 2name is illegal\n"
        "  ❌ no spaces: my name is invalid\n\n"
        "💡 Good variable names = less suffering at 2am debugging 🌙"
    ),

    "data type": (
        "🗂️ DATA TYPES — Python needs to know WHAT kind of thing you're storing.\n\n"
        "Python is dynamically typed (it guesses the type — usually correctly 😅)\n\n"
        "```python\n"
        "x  = 42           # int   — whole numbers: -5, 0, 100\n"
        "y  = 3.14         # float — decimals: 1.5, -0.01, 99.9\n"
        "s  = 'hello'      # str   — text, always in quotes\n"
        "b  = True         # bool  — ONLY True or False (capital T/F!)\n"
        "n  = None         # NoneType — nothing. Emptiness. The void.\n"
        "\n"
        "# Check the type\n"
        "print(type(42))       # <class 'int'>\n"
        "print(type('hi'))     # <class 'str'>\n"
        "print(type(3.14))     # <class 'float'>\n"
        "\n"
        "# Type conversion\n"
        "print(int('5'))       # '5' → 5\n"
        "print(str(100))       # 100 → '100'\n"
        "print(float(3))       # 3 → 3.0\n"
        "```\n\n"
        "⚠️ Mixing types carelessly = TypeError. Python will not let it slide."
    ),

    "if": (
        "🚦 IF / ELIF / ELSE — decision making in code!\n\n"
        "Your program asks: is this condition True? Then do THIS.\n"
        "Otherwise do THAT. Just like deciding whether to exercise 🏋️\n"
        "(If motivated → gym. Elif slightly motivated → walk. Else → Netflix.)\n\n"
        "```python\n"
        "score = 75\n"
        "\n"
        "if score >= 90:\n"
        "    print('A — Outstanding! 🏆')\n"
        "elif score >= 70:\n"
        "    print('B — Solid work! Keep going 💪')\n"
        "elif score >= 50:\n"
        "    print('C — Passing, but push harder 📚')\n"
        "else:\n"
        "    print('F — Okay, let us revisit this together 🤝')\n"
        "# Output: B — Solid work! Keep going 💪\n"
        "```\n\n"
        "Comparison operators:\n"
        "  ==  equal to         !=  not equal to\n"
        "  >   greater than     <   less than\n"
        "  >=  greater or equal <=  less or equal\n\n"
        "Logical operators: and, or, not\n\n"
        "🚨 INDENTATION IS NOT OPTIONAL. Python uses spaces to understand structure.\n"
        "Miss it → IndentationError → regret → learning experience."
    ),

    "loop": (
        "🔄 LOOPS — for when copy-pasting is beneath your dignity.\n\n"
        "Two types:\n"
        "  • for   — 'I know exactly how many times'\n"
        "  • while — 'I'll stop eventually... probably'\n\n"
        "```python\n"
        "# FOR loop — iterate over a sequence\n"
        "fruits = ['apple', 'banana', 'mango']\n"
        "for fruit in fruits:\n"
        "    print('I love', fruit)\n"
        "\n"
        "# range() — gives numbers on demand\n"
        "for i in range(5):     # 0, 1, 2, 3, 4\n"
        "    print(i, end=' ')  # prints: 0 1 2 3 4\n"
        "\n"
        "for i in range(1, 10, 2):  # start=1, stop=10, step=2\n"
        "    print(i, end=' ')      # prints: 1 3 5 7 9\n"
        "\n"
        "# WHILE loop — runs until condition is False\n"
        "count = 0\n"
        "while count < 5:\n"
        "    print('Count:', count)\n"
        "    count += 1   # ← CRITICAL. Forget this = infinite loop 😱\n"
        "\n"
        "# break and continue\n"
        "for n in range(10):\n"
        "    if n == 3: continue   # skip 3\n"
        "    if n == 7: break      # stop at 7\n"
        "    print(n, end=' ')     # 0 1 2 4 5 6\n"
        "```\n\n"
        "⚠️ Infinite loops: technically impressive, practically catastrophic."
    ),

    "function": (
        "🧩 FUNCTIONS — write once, use forever. The ultimate laziness (in a good way).\n\n"
        "Instead of repeating code 50 times like a cave person,\n"
        "you wrap it in a function, give it a name, and call it. Clean. Elegant. Smart.\n\n"
        "```python\n"
        "# Define with 'def'\n"
        "def greet(name):\n"
        "    message = f'Hello, {name}! Ready to code? 🚀'\n"
        "    return message\n"
        "\n"
        "# Call it\n"
        "print(greet('Alice'))   # Hello, Alice! Ready to code? 🚀\n"
        "print(greet('Bob'))     # Hello, Bob! Ready to code? 🚀\n"
        "\n"
        "# Default parameters\n"
        "def power(base, exp=2):\n"
        "    return base ** exp\n"
        "\n"
        "print(power(3))      # 9  (exp defaults to 2)\n"
        "print(power(2, 10))  # 1024\n"
        "\n"
        "# Multiple return values\n"
        "def min_max(numbers):\n"
        "    return min(numbers), max(numbers)\n"
        "\n"
        "lo, hi = min_max([3, 1, 4, 1, 5, 9])\n"
        "print(lo, hi)  # 1  9\n"
        "```\n\n"
        "Golden rule: one function → one job.\n"
        "A function doing 12 things = a disaster pretending to be code."
    ),

    "list": (
        "📋 LISTS — ordered, changeable collections of anything.\n\n"
        "Python lists are like backpacks — shove anything in, any order, any size.\n\n"
        "```python\n"
        "nums   = [1, 2, 3, 4, 5]\n"
        "mixed  = [42, 'hello', True, 3.14]   # mixing types is fine!\n"
        "empty  = []\n"
        "\n"
        "# Indexing — starts at 0 (not 1, never 1)\n"
        "print(nums[0])    # 1  ← first item\n"
        "print(nums[-1])   # 5  ← last item\n"
        "print(nums[1:4])  # [2, 3, 4]  ← slicing\n"
        "print(nums[::-1]) # [5, 4, 3, 2, 1]  ← reversed!\n"
        "\n"
        "# Common methods\n"
        "nums.append(6)         # add to end\n"
        "nums.insert(0, 0)      # insert at position\n"
        "nums.pop()             # remove and return last item\n"
        "nums.remove(3)         # remove first occurrence of 3\n"
        "nums.sort()            # sort in place\n"
        "nums.reverse()         # reverse in place\n"
        "print(len(nums))       # length of list\n"
        "print(3 in nums)       # True/False — is 3 in the list?\n"
        "```\n\n"
        "Lists are MUTABLE — you can change them after creation.\n"
        "Unlike some people's opinions. Lists are more flexible."
    ),

    "tuple": (
        "🔒 TUPLES — like lists, but they CANNOT be changed. Permanent. Decisive.\n\n"
        "Use tuples when data should never change: coordinates, colours, settings.\n\n"
        "```python\n"
        "point      = (3, 4)          # a 2D coordinate\n"
        "rgb        = (255, 128, 0)   # an orange colour\n"
        "days       = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri')\n"
        "single     = (42,)           # ONE-item tuple needs trailing comma!\n"
        "\n"
        "print(point[0])   # 3\n"
        "print(len(days))  # 5\n"
        "\n"
        "# Tuple unpacking (really useful!)\n"
        "x, y = point\n"
        "print(x, y)   # 3  4\n"
        "\n"
        "a, b, c = 1, 2, 3   # Also tuple unpacking\n"
        "\n"
        "# Swap variables without a temp variable!\n"
        "a, b = b, a         # Python magic ✨\n"
        "\n"
        "# point[0] = 99  → TypeError! Tuples don't change.\n"
        "```\n\n"
        "Tuples are faster than lists and signal 'this data is sacred'.\n"
        "Choose wisely: list = flexible, tuple = final."
    ),

    "set": (
        "🎯 SETS — unordered collections with NO duplicates.\n\n"
        "Sets automatically remove duplicates. They're the bouncers of data structures —\n"
        "if you're already inside, you're not getting in again. 🚫\n\n"
        "```python\n"
        "fruits = {'apple', 'banana', 'mango', 'apple'}  # apple only once!\n"
        "print(fruits)   # {'apple', 'banana', 'mango'} — order varies!\n"
        "\n"
        "# From a list — removes duplicates instantly\n"
        "nums = [1, 2, 2, 3, 3, 3, 4]\n"
        "unique = set(nums)\n"
        "print(unique)   # {1, 2, 3, 4}\n"
        "\n"
        "# Set operations — like Venn diagrams!\n"
        "a = {1, 2, 3, 4}\n"
        "b = {3, 4, 5, 6}\n"
        "\n"
        "print(a | b)   # Union:        {1, 2, 3, 4, 5, 6}\n"
        "print(a & b)   # Intersection: {3, 4}\n"
        "print(a - b)   # Difference:   {1, 2}\n"
        "print(a ^ b)   # Symmetric diff: {1, 2, 5, 6}\n"
        "\n"
        "a.add('hello')    # add element\n"
        "a.discard(99)     # remove safely (no error if missing)\n"
        "```\n\n"
        "Sets are great for membership testing (very fast!) and removing duplicates."
    ),

    "dictionary": (
        "📖 DICTIONARIES — key-value pairs. Like a real dictionary but actually useful.\n\n"
        "Instead of 'item 3', you ask 'give me the value for this KEY'.\n"
        "Perfect for structured data — think: a student's profile, a product, a config.\n\n"
        "```python\n"
        "student = {\n"
        "    'name'  : 'Alice',\n"
        "    'age'   : 21,\n"
        "    'grade' : 'A',\n"
        "    'active': True\n"
        "}\n"
        "\n"
        "# Access\n"
        "print(student['name'])              # Alice\n"
        "print(student.get('age', 0))        # 21 (safe — won't crash!)\n"
        "\n"
        "# Add / update\n"
        "student['score'] = 95\n"
        "student['grade'] = 'A+'\n"
        "\n"
        "# Looping\n"
        "for key, value in student.items():\n"
        "    print(f'{key}: {value}')\n"
        "\n"
        "print(student.keys())    # dict_keys(['name', 'age', ...])\n"
        "print(student.values())  # dict_values(['Alice', 21, ...])\n"
        "\n"
        "# Check if key exists\n"
        "if 'name' in student:\n"
        "    print('Name found!')\n"
        "```\n\n"
        "Keys must be UNIQUE and IMMUTABLE (strings, numbers, tuples — no lists as keys).\n"
        "Duplicate key = last value wins. Drama: resolved."
    ),

    "string": (
        "🔤 STRINGS — text in Python. Lives between quotes. Very popular at parties.\n\n"
        "Single 'quotes', double \"quotes\", triple '''quotes''' — all fine.\n"
        "Python's very accepting like that 😌\n\n"
        "```python\n"
        "s = 'Hello, World!'\n"
        "\n"
        "# Common methods\n"
        "print(s.upper())               # HELLO, WORLD!\n"
        "print(s.lower())               # hello, world!\n"
        "print(s.title())               # Hello, World!\n"
        "print(s.replace('World', 'Python'))  # Hello, Python!\n"
        "print(s.split(', '))           # ['Hello', 'World!']\n"
        "print(s.strip())               # removes whitespace at edges\n"
        "print(s.startswith('Hello'))   # True\n"
        "print(len(s))                  # 13\n"
        "print(s[0])                    # H  (indexing works like lists!)\n"
        "\n"
        "# f-strings — the modern beautiful way ✨\n"
        "name = 'Alice'\n"
        "age  = 21\n"
        "print(f'{name} is {age} years old and {age*2} in dog years')\n"
        "\n"
        "# Multi-line string\n"
        "message = '''Line one\n"
        "Line two\n"
        "Line three'''\n"
        "```\n\n"
        "Strings are IMMUTABLE — you can't change characters in place.\n"
        "To 'modify' a string, you create a new one. Very principled."
    ),

    "class": (
        "🏗️ CLASSES — blueprints for creating objects. Welcome to OOP!\n\n"
        "A class is like a cookie cutter 🍪\n"
        "The class = the cutter shape. Each object = an individual cookie.\n"
        "Same structure, different values. Elegant and powerful.\n\n"
        "```python\n"
        "class Student:\n"
        "    # Class variable — shared by ALL students\n"
        "    school = 'Python Academy'\n"
        "\n"
        "    # __init__ runs when you CREATE a Student\n"
        "    def __init__(self, name, grade):\n"
        "        self.name  = name    # instance attribute\n"
        "        self.grade = grade\n"
        "        self.score = 0\n"
        "\n"
        "    def study(self, hours):\n"
        "        self.score += hours * 10\n"
        "        return f'{self.name} studied {hours}h → score: {self.score}'\n"
        "\n"
        "    def __str__(self):  # what print() shows\n"
        "        return f'Student({self.name}, Grade {self.grade})'\n"
        "\n"
        "# Create instances\n"
        "s1 = Student('Alice', 'A')\n"
        "s2 = Student('Bob',   'B')\n"
        "\n"
        "print(s1)               # Student(Alice, Grade A)\n"
        "print(s1.study(3))      # Alice studied 3h → score: 30\n"
        "print(Student.school)   # Python Academy\n"
        "```\n\n"
        "'self' = the object itself. Python's way of saying 'this specific one'."
    ),

    "inheritance": (
        "👨‍👩‍👧 INHERITANCE — child classes inherit from parent classes.\n\n"
        "Write a general base class, then build SPECIALISED versions.\n"
        "Don't repeat yourself — that's a crime in clean code.\n\n"
        "```python\n"
        "class Animal:\n"
        "    def __init__(self, name):\n"
        "        self.name = name\n"
        "\n"
        "    def speak(self):\n"
        "        return f'{self.name} makes a sound'\n"
        "\n"
        "    def __str__(self):\n"
        "        return f'Animal: {self.name}'\n"
        "\n"
        "# Child class inherits from Animal\n"
        "class Dog(Animal):\n"
        "    def speak(self):            # override parent method\n"
        "        return f'{self.name} says: WOOF! 🐕'\n"
        "\n"
        "class Cat(Animal):\n"
        "    def speak(self):\n"
        "        return f'{self.name} says: meow... 🐱'\n"
        "\n"
        "class Duck(Animal):\n"
        "    def speak(self):\n"
        "        return f'{self.name} says: quack 🦆'\n"
        "\n"
        "animals = [Dog('Buddy'), Cat('Luna'), Duck('Donald')]\n"
        "for a in animals:\n"
        "    print(a.speak())    # each speaks differently!\n"
        "```\n\n"
        "This is called POLYMORPHISM — same method name, different behaviour.\n"
        "Beautiful, isn't it? Like children who surprise you. 😄"
    ),

    "error": (
        "🚨 EXCEPTION HANDLING — catching errors before they ruin your day.\n\n"
        "Errors WILL happen. The question is: does your program crash gracefully\n"
        "or does it just explode with a stack trace? 💥\n\n"
        "```python\n"
        "# Basic try/except\n"
        "try:\n"
        "    result = 10 / 0          # ZeroDivisionError!\n"
        "except ZeroDivisionError:\n"
        "    print('Cannot divide by zero! Math rules still apply 😅')\n"
        "\n"
        "# Catch multiple types\n"
        "try:\n"
        "    num = int('not-a-number') # ValueError!\n"
        "except ValueError:\n"
        "    print('That is not a number!')\n"
        "except TypeError as e:\n"
        "    print(f'Type issue: {e}')\n"
        "except Exception as e:       # catch-all\n"
        "    print(f'Something broke: {e}')\n"
        "finally:                      # ALWAYS runs\n"
        "    print('Cleanup complete ✅')\n"
        "\n"
        "# Raise your own errors\n"
        "def set_age(age):\n"
        "    if age < 0:\n"
        "        raise ValueError('Age cannot be negative!')\n"
        "    if age > 150:\n"
        "        raise ValueError('Are you a vampire? 🧛')\n"
        "    return age\n"
        "```\n\n"
        "Common exceptions: ValueError, TypeError, IndexError,\n"
        "KeyError, FileNotFoundError, ZeroDivisionError, AttributeError."
    ),

    "import": (
        "📦 IMPORTS — borrowing superpowers from other code.\n\n"
        "Python ships with a massive 'standard library' of free modules.\n"
        "Plus, thousands of third-party packages via pip.\n"
        "You don't have to build EVERYTHING from scratch. That would be exhausting 😤\n\n"
        "```python\n"
        "# Standard library\n"
        "import math\n"
        "print(math.sqrt(16))        # 4.0\n"
        "print(math.pi)              # 3.14159...\n"
        "print(math.ceil(4.2))       # 5\n"
        "\n"
        "import random\n"
        "print(random.randint(1, 10))         # random 1-10\n"
        "print(random.choice(['a', 'b', 'c']))  # random element\n"
        "random.shuffle([1, 2, 3, 4])           # shuffle in place\n"
        "\n"
        "import datetime\n"
        "now = datetime.datetime.now()\n"
        "print(now.strftime('%Y-%m-%d %H:%M'))  # 2025-07-15 14:30\n"
        "\n"
        "import os\n"
        "print(os.getcwd())   # current working directory\n"
        "\n"
        "# Import specific things (cleaner, faster)\n"
        "from math import sqrt, pi\n"
        "print(sqrt(25))  # 5.0 — no 'math.' prefix needed\n"
        "\n"
        "# Aliases\n"
        "import numpy as np       # pip install numpy\n"
        "import pandas as pd      # pip install pandas\n"
        "```"
    ),

    "recursion": (
        "🪆 RECURSION — a function that calls ITSELF. Inception, but for code.\n\n"
        "Every recursive function MUST have:\n"
        "  1. BASE CASE — when to STOP (extremely important, trust me)\n"
        "  2. RECURSIVE CASE — calling itself with a simpler version of the problem\n\n"
        "```python\n"
        "# Factorial: n! = n × (n-1) × (n-2) × ... × 1\n"
        "def factorial(n):\n"
        "    if n == 0 or n == 1:        # BASE CASE: stop here\n"
        "        return 1\n"
        "    return n * factorial(n - 1) # RECURSIVE CASE\n"
        "\n"
        "print(factorial(5))   # 5×4×3×2×1 = 120\n"
        "\n"
        "# Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13...\n"
        "def fib(n):\n"
        "    if n <= 1:              # BASE CASE\n"
        "        return n\n"
        "    return fib(n-1) + fib(n-2)\n"
        "\n"
        "print([fib(i) for i in range(8)])  # [0,1,1,2,3,5,8,13]\n"
        "\n"
        "# Count down\n"
        "def countdown(n):\n"
        "    if n <= 0:\n"
        "        print('Blast off! 🚀')\n"
        "        return\n"
        "    print(n)\n"
        "    countdown(n - 1)\n"
        "\n"
        "countdown(5)   # 5 4 3 2 1 Blast off!\n"
        "```\n\n"
        "⚠️ No base case = RecursionError (Python quits after ~1000 calls).\n"
        "Python's polite way of saying: please use a loop for this one."
    ),

    "comprehension": (
        "⚡ COMPREHENSIONS — Python's beautiful one-liner list builders.\n\n"
        "Replaces verbose for-loops with elegant, readable expressions.\n"
        "Warning: may cause your non-Python friends to be deeply confused 🧙\n\n"
        "```python\n"
        "# Old way (works, but wordy)\n"
        "squares = []\n"
        "for x in range(1, 6):\n"
        "    squares.append(x ** 2)\n"
        "\n"
        "# List comprehension (elegant!)\n"
        "squares = [x**2 for x in range(1, 6)]\n"
        "print(squares)    # [1, 4, 9, 16, 25]\n"
        "\n"
        "# With filter\n"
        "evens = [x for x in range(20) if x % 2 == 0]\n"
        "print(evens)      # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]\n"
        "\n"
        "# String processing\n"
        "words  = ['hello', 'world', 'python']\n"
        "upper  = [w.upper() for w in words]\n"
        "long_words = [w for w in words if len(w) > 4]\n"
        "\n"
        "# Dict comprehension\n"
        "word_lengths = {w: len(w) for w in words}\n"
        "# {'hello': 5, 'world': 5, 'python': 6}\n"
        "\n"
        "# Set comprehension\n"
        "unique_mods = {x % 4 for x in range(12)}\n"
        "# {0, 1, 2, 3}\n"
        "```"
    ),

    "lambda": (
        "λ LAMBDA — tiny, anonymous, one-liner functions.\n\n"
        "Use when the function is too small to deserve a proper name.\n"
        "Like a sticky note vs. an official memo — both useful, different scale.\n\n"
        "```python\n"
        "# Regular function\n"
        "def double(x):\n"
        "    return x * 2\n"
        "\n"
        "# Identical as lambda\n"
        "double = lambda x: x * 2\n"
        "print(double(5))         # 10\n"
        "\n"
        "# Multiple arguments\n"
        "add = lambda a, b: a + b\n"
        "print(add(3, 4))         # 7\n"
        "\n"
        "# Most powerful with sorted/filter/map\n"
        "names = ['Charlie', 'Alice', 'Bob', 'Dan']\n"
        "names.sort(key=lambda n: len(n))    # sort by name length\n"
        "print(names)  # ['Bob', 'Dan', 'Alice', 'Charlie']\n"
        "\n"
        "students = [('Alice', 90), ('Bob', 75), ('Eve', 95)]\n"
        "students.sort(key=lambda s: s[1], reverse=True)  # sort by grade\n"
        "print(students)  # [('Eve', 95), ('Alice', 90), ('Bob', 75)]\n"
        "\n"
        "# filter() — keep only matching items\n"
        "nums = [1, 2, 3, 4, 5, 6]\n"
        "evens = list(filter(lambda x: x % 2 == 0, nums))\n"
        "print(evens)  # [2, 4, 6]\n"
        "\n"
        "# map() — transform every item\n"
        "doubled = list(map(lambda x: x * 2, nums))\n"
        "print(doubled)  # [2, 4, 6, 8, 10, 12]\n"
        "```"
    ),

    "algorithm": (
        "🧮 ALGORITHMS — step-by-step instructions to solve a problem.\n\n"
        "An algorithm is NOT code — it's a STRATEGY.\n"
        "Code is how you implement that strategy in a specific language.\n\n"
        "Properties of a good algorithm:\n"
        "  ✅ Correct — gives the right answer\n"
        "  ✅ Efficient — doesn't waste time or memory\n"
        "  ✅ Clear — understandable by humans\n"
        "  ✅ Finite — STOPS eventually (crucial!)\n\n"
        "Famous algorithms in Python:\n\n"
        "```python\n"
        "# LINEAR SEARCH — check each item one by one\n"
        "def linear_search(lst, target):\n"
        "    for i, item in enumerate(lst):\n"
        "        if item == target:\n"
        "            return i   # found at index i\n"
        "    return -1          # not found\n"
        "\n"
        "# BUBBLE SORT — repeatedly swap adjacent wrong-order pairs\n"
        "def bubble_sort(lst):\n"
        "    n = len(lst)\n"
        "    for i in range(n):\n"
        "        for j in range(0, n-i-1):\n"
        "            if lst[j] > lst[j+1]:\n"
        "                lst[j], lst[j+1] = lst[j+1], lst[j]  # swap!\n"
        "    return lst\n"
        "\n"
        "print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))\n"
        "# [11, 12, 22, 25, 34, 64, 90]\n"
        "```\n\n"
        "Time complexity (Big O) — how performance scales with input size:\n"
        "  O(1) — constant: always same speed ⚡\n"
        "  O(n) — linear: doubles when input doubles\n"
        "  O(n²) — quadratic: gets slow FAST 🐢"
    ),

    "file": (
        "📁 FILE HANDLING — reading and writing files in Python.\n\n"
        "Programs often need to save data or read from files.\n"
        "Python makes this surprisingly painless!\n\n"
        "```python\n"
        "# WRITING a file\n"
        "with open('notes.txt', 'w') as f:\n"
        "    f.write('Hello, file world!\\n')\n"
        "    f.write('Second line here.\\n')\n"
        "\n"
        "# READING a file\n"
        "with open('notes.txt', 'r') as f:\n"
        "    content = f.read()       # reads entire file\n"
        "    print(content)\n"
        "\n"
        "# Read line by line\n"
        "with open('notes.txt', 'r') as f:\n"
        "    for line in f:\n"
        "        print(line.strip())  # strip removes newline\n"
        "\n"
        "# APPENDING (add without erasing)\n"
        "with open('notes.txt', 'a') as f:\n"
        "    f.write('Third line added later!\\n')\n"
        "\n"
        "# Read into a list of lines\n"
        "with open('notes.txt', 'r') as f:\n"
        "    lines = f.readlines()   # list of strings\n"
        "```\n\n"
        "File modes:\n"
        "  'r' — read only (default)\n"
        "  'w' — write (creates or OVERWRITES!)\n"
        "  'a' — append (adds to end)\n"
        "  'x' — create (fails if file exists)\n\n"
        "Always use 'with' — it closes the file automatically. No messy cleanup."
    ),

    "scope": (
        "🔭 SCOPE — where variables are visible and accessible.\n\n"
        "Not all variables are visible everywhere!\n"
        "Python uses LEGB rule to find variables:\n\n"
        "  L — Local      (inside current function)\n"
        "  E — Enclosing  (outer function, if nested)\n"
        "  G — Global     (module level)\n"
        "  B — Built-in   (Python's built-ins: print, len, etc.)\n\n"
        "```python\n"
        "x = 'global'     # GLOBAL scope\n"
        "\n"
        "def outer():\n"
        "    x = 'enclosing'   # ENCLOSING scope\n"
        "\n"
        "    def inner():\n"
        "        x = 'local'   # LOCAL scope\n"
        "        print(x)      # local wins: 'local'\n"
        "\n"
        "    inner()\n"
        "    print(x)          # enclosing: 'enclosing'\n"
        "\n"
        "outer()\n"
        "print(x)              # global: 'global'\n"
        "\n"
        "# global keyword — use (but don't abuse!)\n"
        "count = 0\n"
        "def increment():\n"
        "    global count\n"
        "    count += 1\n"
        "```\n\n"
        "Local variables die when the function ends.\n"
        "Global variables live until the program ends.\n"
        "Use globals sparingly — they make code harder to reason about."
    ),
}

# ── keyword → topic key mapping 
keywords = {
    "computer"          : "what is a computer",
    "what is a computer": "what is a computer",
    "hardware"          : "hardware",
    "cpu"               : "hardware",
    "ram"               : "hardware",
    "processor"         : "hardware",
    "memory"            : "hardware",
    "software"          : "software",
    "application"       : "software",
    "app"               : "software",
    "operating system"  : "operating system",
    "os"                : "operating system",
    "windows"           : "operating system",
    "linux"             : "operating system",
    "binary"            : "binary",
    "bit"               : "binary",
    "byte"              : "binary",
    "internet"          : "internet",
    "network"           : "internet",
    "ip address"        : "internet",
    "what is python"    : "what is python",
    "python history"    : "python history",
    "python"            : "what is python",
    "variable"          : "variable",
    "variables"         : "variable",
    "data type"         : "data type",
    "datatype"          : "data type",
    "int"               : "data type",
    "float"             : "data type",
    "bool"              : "data type",
    "if"                : "if",
    "else"              : "if",
    "elif"              : "if",
    "condition"         : "if",
    "loop"              : "loop",
    "for loop"          : "loop",
    "while"             : "loop",
    "iterate"           : "loop",
    "function"          : "function",
    "def "              : "function",
    "return"            : "function",
    "list"              : "list",
    "array"             : "list",
    "tuple"             : "tuple",
    "set"               : "set",
    "dictionary"        : "dictionary",
    "dict"              : "dictionary",
    "string"            : "string",
    "str"               : "string",
    "text"              : "string",
    "class"             : "class",
    "object"            : "class",
    "oop"               : "class",
    "inheritance"       : "inheritance",
    "inherit"           : "inheritance",
    "error"             : "error",
    "exception"         : "error",
    "try"               : "error",
    "except"            : "error",
    "import"            : "import",
    "module"            : "import",
    "library"           : "import",
    "package"           : "import",
    "recursion"         : "recursion",
    "recursive"         : "recursion",
    "comprehension"     : "comprehension",
    "list comp"         : "comprehension",
    "lambda"            : "lambda",
    "algorithm"         : "algorithm",
    "sort"              : "algorithm",
    "search"            : "algorithm",
    "file"              : "file",
    "read file"         : "file",
    "write file"        : "file",
    "scope"             : "scope",
    "global"            : "scope",
    "local"             : "scope",
}

jokes = [
    ("Why don't programmers like nature?",          "It has too many bugs 🐛"),
    ("What's a computer's favourite snack?",         "Microchips 🍟"),
    ("Why was the JavaScript developer sad?",        "He didn't know how to 'null' his feelings 💔"),
    ("How many programmers to change a light bulb?", "None — that's a hardware problem 💡"),
    ("Why do Python devs wear glasses?",             "Because they can't C# 🕶️"),
    ("Why did the developer go broke?",              "He used up all his cache 💸"),
    ("Why is Python so calm?",                       "Because it never has to deal with semicolons 😌"),
    ("What do you call a snake that's 3.14m long?",  "A π-thon 🐍"),
    ("Why do programmers prefer dark mode?",         "Because light attracts bugs! 🪲"),
    ("What did the Python say to the JavaScript?",   "You don't need semicolons. Let it go. 🎵"),
]

puns = [
    "I was going to tell you a UDP joke, but you might not get it 📡",
    "There are 10 kinds of people: those who understand binary, and those who don't 🔢",
    "A SQL query walks into a bar and asks two tables: 'Can I JOIN you?' 🍻",
    "I would tell you a TCP joke but I'd repeat it until you acknowledged it 📶",
    "Python called. It says your indentation is a war crime 📐",
    "Why can't you trust atoms? They make up everything — just like your test excuses 😂",
]

greetings_responses = [
    "Hey! 👋 Welcome to PyBuddy! Type 'help' to see all topics!",
    "Hello there, future programmer! 😊 Ready to learn Python and computer basics?",
    "Greetings! 🎉 I'm PyBuddy, your friendly coding tutor. Ask me anything!",
    "Hi! 🐍 Great to see you! Ask about Python, computer basics, or type 'help'.",
]

farewell_responses = [
    "Goodbye! May your code be bug-free 🍀 (It won't be, but the thought counts!)",
    "See you later! May your loops always terminate and your variables be meaningful 👋",
    "Bye! Keep coding — you're doing better than you think 😊",
    "Take care! Come back anytime — PyBuddy will be here, endlessly patient 🤖",
]

compliments = [
    "Thank you! That's very kind 😊 Now ask me a Python question so we can celebrate properly!",
    "You're too nice! Go channel that positivity into writing some code 💻",
    "Appreciate it! Now, shall we learn something amazing? 🚀",
    "Thank you! You just made a chatbot's day. Seriously. 😄",
]

encouragements = [
    "You're doing great! Every expert was once a beginner 💪",
    "Learning takes time — be patient with yourself. You've got this! 🌟",
    "Confused is just 'about to understand'. Keep going! 🧩",
    "Every bug you encounter is a lesson in disguise 🐛→🦋",
]

joke_state = {}


def get_response(user_input: str) -> str:
    raw  = user_input.strip()
    text = raw.lower()

    if joke_state.get("waiting"):
        joke_state["waiting"] = False
        return "🥁 " + joke_state.pop("punchline", "...I forgot the punchline 😅")

    if any(w in text for w in ["hello", "hi", "hey", "sup", "howdy", "hola",
                                "assalam", "salam", "good morning", "good afternoon"]):
        return random.choice(greetings_responses)

    if any(w in text for w in ["bye", "goodbye", "cya", "see ya", "later",
                                "farewell", "khuda hafiz", "allah hafiz"]):
        return random.choice(farewell_responses)

    if "your name" in text or "who are you" in text or "what are you" in text:
        return ("🐍 I'm PyBuddy — your Python & Computer Science Fundamentals Tutor!\n\n"
                "I can teach you:\n"
                "  💻 Computer basics (hardware, software, OS, binary)\n"
                "  🐍 Python programming (variables to classes)\n"
                "  🧮 Programming fundamentals (loops, functions, algorithms)\n\n"
                "Type 'help' to see everything I can teach! 📚")

    if "time" in text and "data" not in text:
        t = datetime.datetime.now().strftime("%I:%M:%S %p")
        return f"⏰ Current time: {t}\n\nNow stop procrastinating and go write some code! 😄"

    if "date" in text or "today" in text:
        d = datetime.datetime.now().strftime("%A, %d %B %Y")
        return f"📅 Today is {d}!\n\nAnother wonderful day to learn Python 🎊"

    if "joke" in text or "funny" in text or "laugh" in text:
        setup, punchline = random.choice(jokes)
        joke_state["waiting"]   = True
        joke_state["punchline"] = punchline
        return f"😄 {setup}\n\n*(Type anything for the punchline...)*"

    if "pun" in text:
        return random.choice(puns)

    if any(w in text for w in ["hard", "difficult", "struggling", "confused",
                                "don't understand", "dont understand", "help me"]):
        base = random.choice(encouragements)
        return base + "\n\nTry asking: 'what is a variable?' or 'explain functions' 😊"

    sorted_keywords = sorted(keywords.keys(), key=len, reverse=True)
    for keyword in sorted_keywords:
        if keyword in text:
            return knowledge[keywords[keyword]]

    if any(p in text for p in ["what is", "explain", "teach", "how does",
                                "how do", "tell me about", "define", "what are"]):
        if wikipedia:
            try:
                topic = (text.replace("what is", "").replace("explain", "")
                             .replace("teach me about", "").replace("how does", "")
                             .replace("how do", "").replace("tell me about", "")
                             .replace("define", "").replace("what are", "").strip())
                result = wikipedia.summary(topic, sentences=2)
                return f"📚 {result}\n\n*(Source: Wikipedia)*"
            except Exception:
                pass
        return ("🤔 I don't have that topic in my notes yet!\n\n"
                "I can teach you about:\n"
                "Computer: hardware, software, OS, binary, internet\n"
                "Python: variable, list, tuple, set, dictionary, string,\n"
                "        function, class, inheritance, loop, if/else,\n"
                "        error handling, import, recursion, lambda,\n"
                "        comprehension, algorithm, file, scope\n\n"
                "Type 'help' for the full menu! 📋")

    if any(w in text for w in ["love", "great", "awesome", "amazing",
                                "best", "cool", "nice", "good bot", "helpful"]):
        return random.choice(compliments)

    if any(w in text for w in ["hate", "stupid", "dumb", "useless", "bad", "worst", "terrible"]):
        return ("I understand the frustration! 😊 Programming is genuinely hard sometimes.\n\n"
                "Let's try a fresh start — what topic would you like to learn?\n"
                "Type 'help' to see all available topics 📚")

    if "help" in text or "what can you" in text or "topics" in text or "menu" in text:
        return (
            "📚 COMPLETE TOPICS MENU\n\n"
            "💻 COMPUTER BASICS:\n"
            "  computer  |  hardware  |  software\n"
            "  operating system  |  binary  |  internet\n\n"
            "🐍 PYTHON LANGUAGE:\n"
            "  what is python  |  python history\n\n"
            "📦 DATA & VARIABLES:\n"
            "  variable  |  data type  |  string\n"
            "  list  |  tuple  |  set  |  dictionary\n\n"
            "🔧 CONTROL FLOW:\n"
            "  if / else  |  loop  |  recursion\n\n"
            "🧩 FUNCTIONS & STRUCTURE:\n"
            "  function  |  lambda  |  comprehension\n"
            "  scope  |  import\n\n"
            "🏗️ OOP (Object-Oriented):\n"
            "  class  |  inheritance\n\n"
            "🛠️ PRACTICAL:\n"
            "  error handling  |  file handling  |  algorithm\n\n"
            "🎭 FUN:\n"
            "  joke  |  pun  |  time  |  date"
        )

    if "meaning of life" in text or "42" in text:
        return "42. Confirmed.\n\nIn Python:\n  answer = 6 * 7\n  print(answer)  # 42 🐍"

    return ("Hmm, I didn't catch that! 🤔\n\n"
            "Try asking about a specific topic like:\n"
            "'What is a variable?' or 'Explain functions'\n\n"
            "Type 'help' to see everything I can teach! 📚")

#   GUI — PYTHON-INSPIRED DARK THEME

class ChatApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("PyBuddy 🐍 — Python & CS Fundamentals Tutor")
        self.root.geometry("800x880")
        self.root.minsize(580, 660)
        self.root.configure(bg=BG_MAIN)
        self.root.resizable(True, True)

        # ── Times New Roman fonts ──
        self.font_title  = tkfont.Font(family="Times New Roman", size=15, weight="bold")
        self.font_msg    = tkfont.Font(family="Times New Roman", size=11)
        self.font_name   = tkfont.Font(family="Times New Roman", size=10, weight="bold")
        self.font_sub    = tkfont.Font(family="Times New Roman", size=9)
        self.font_entry  = tkfont.Font(family="Times New Roman", size=13)
        self.font_btn    = tkfont.Font(family="Times New Roman", size=12, weight="bold")
        self.font_status = tkfont.Font(family="Times New Roman", size=10)

        self._build_ui()
        self._animate_header()
        self._post_welcome()

    def _build_ui(self):
        # ── header ──
        self.header = tk.Frame(self.root, bg=BG_PANEL, height=84)
        self.header.pack(fill=tk.X, side=tk.TOP)
        self.header.pack_propagate(False)

        # Python logo colours — blue circle + yellow circle side by side
        logo_frame = tk.Frame(self.header, bg=BG_PANEL)
        logo_frame.pack(side=tk.LEFT, padx=(16, 6), pady=10)

        tk.Label(
            logo_frame, text="🐍",
            font=tkfont.Font(family="Times New Roman", size=36),
            bg=BG_PANEL, fg=ACCENT_YELLOW
        ).pack()

        hinfo = tk.Frame(self.header, bg=BG_PANEL)
        hinfo.pack(side=tk.LEFT, pady=10)

        self.title_lbl = tk.Label(
            hinfo, text="PyBuddy",
            font=self.font_title, bg=BG_PANEL, fg=ACCENT_YELLOW
        )
        self.title_lbl.pack(anchor="w")

        self.status_lbl = tk.Label(
            hinfo, text="● Online  •  Python & CS Fundamentals Tutor",
            font=self.font_status, bg=BG_PANEL, fg=ACCENT_BLUE
        )
        self.status_lbl.pack(anchor="w")

        # ── gradient-style top divider — Python blue + yellow stripe ──
        div = tk.Frame(self.root, bg=BG_PANEL)
        div.pack(fill=tk.X)
        tk.Frame(div, bg=ACCENT_BLUE,   height=3).pack(fill=tk.X)
        tk.Frame(div, bg=ACCENT_YELLOW, height=3).pack(fill=tk.X)

        # ── chat area ──
        chat_frame = tk.Frame(self.root, bg=BG_MAIN)
        chat_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(10, 0))

        self.scrollbar = tk.Scrollbar(chat_frame, bg=BORDER,
                                      troughcolor=BG_MAIN, width=8,
                                      activebackground=ACCENT_YELLOW)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas = tk.Canvas(
            chat_frame, bg=BG_MAIN, highlightthickness=0,
            yscrollcommand=self.scrollbar.set
        )
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.canvas.yview)

        self.msg_frame = tk.Frame(self.canvas, bg=BG_MAIN)
        self.canvas_window = self.canvas.create_window(
            (0, 0), window=self.msg_frame, anchor="nw"
        )
        self.msg_frame.bind("<Configure>",  self._on_frame_configure)
        self.canvas.bind("<Configure>",     self._on_canvas_configure)
        self.canvas.bind("<MouseWheel>",    self._on_mousewheel)
        self.msg_frame.bind("<MouseWheel>", self._on_mousewheel)

        # ── typing indicator ──
        self.typing_var = tk.StringVar(value="")
        tk.Label(
            self.root, textvariable=self.typing_var,
            font=self.font_status, bg=BG_MAIN, fg=ACCENT_YELLOW, anchor="w"
        ).pack(fill=tk.X, padx=16, pady=(4, 0))

        # ── double divider before input ──
        tk.Frame(self.root, bg=ACCENT_YELLOW, height=2).pack(fill=tk.X, pady=(4, 0))
        tk.Frame(self.root, bg=ACCENT_BLUE,   height=2).pack(fill=tk.X)

        # ── input row — full height, well-padded ──
        input_frame = tk.Frame(self.root, bg=BG_PANEL, pady=14)
        input_frame.pack(fill=tk.X, side=tk.BOTTOM)

        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(
            input_frame, textvariable=self.entry_var,
            font=self.font_entry,
            bg=ENTRY_BG, fg=TEXT_DARK,
            insertbackground=ACCENT_YELLOW,
            relief=tk.FLAT,
            highlightthickness=2,
            highlightcolor=ACCENT_YELLOW,
            highlightbackground=BORDER
        )
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True,
                        padx=(16, 10), ipady=13)   # ipady=13 → tall input field
        self.entry.bind("<Return>",     lambda e: self._on_send())
        self.entry.bind("<KeyRelease>", self._on_key)
        self.entry.focus_set()

        self.send_btn = tk.Button(
            input_frame, text="Send  ➤",
            font=self.font_btn,
            bg=ACCENT_YELLOW, fg="#1e1e2e",
            relief=tk.FLAT,
            activebackground=ACCENT_BLUE,
            activeforeground="#ffffff",
            cursor="hand2",
            padx=22, pady=12,
            command=self._on_send
        )
        self.send_btn.pack(side=tk.RIGHT, padx=(0, 16))
        self.send_btn.bind("<Enter>", lambda e: self.send_btn.config(
            bg=ACCENT_BLUE, fg="#ffffff"))
        self.send_btn.bind("<Leave>", lambda e: self.send_btn.config(
            bg=ACCENT_YELLOW, fg="#1e1e2e"))

        # ── footer ──
        footer = tk.Frame(self.root, bg=SHADOW, height=24)
        footer.pack(fill=tk.X, side=tk.BOTTOM)
        tk.Label(
            footer,
            text="PyBuddy  •  Python & CS Fundamentals Tutor  •  Type 'help' to see all topics",
            font=self.font_sub, bg=SHADOW, fg=TEXT_MID
        ).pack(pady=4)

    #  canvas/scroll helpers 

    def _on_frame_configure(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_canvas_configure(self, event):
        self.canvas.itemconfig(self.canvas_window, width=event.width)

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    # ── bubble builder 

    def _add_bubble(self, who: str, text: str, color: str, align: str, icon: str):
        outer = tk.Frame(self.msg_frame, bg=BG_MAIN)
        outer.pack(fill=tk.X, padx=10, pady=6)

        bubble_frame = tk.Frame(outer, bg=BG_MAIN)
        if align == "right":
            bubble_frame.pack(side=tk.RIGHT)
        else:
            bubble_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)

        name_row = tk.Frame(bubble_frame, bg=BG_MAIN)
        name_row.pack(fill=tk.X)

        ts = datetime.datetime.now().strftime("%H:%M")
        if align == "left":
            tk.Label(name_row, text=f"{icon} {who}", font=self.font_name,
                     bg=BG_MAIN, fg=color).pack(side=tk.LEFT)
            tk.Label(name_row, text=ts, font=self.font_sub,
                     bg=BG_MAIN, fg=TEXT_DIM).pack(side=tk.LEFT, padx=6)
        else:
            tk.Label(name_row, text=ts, font=self.font_sub,
                     bg=BG_MAIN, fg=TEXT_DIM).pack(side=tk.RIGHT, padx=6)
            tk.Label(name_row, text=f"{who} {icon}", font=self.font_name,
                     bg=BG_MAIN, fg=color).pack(side=tk.RIGHT)

        bubble_bg = BG_BUBBLE_U if align == "right" else BG_BUBBLE_B
        bar_color = ACCENT_YELLOW if align == "right" else ACCENT_BLUE

        bubble = tk.Frame(bubble_frame, bg=bubble_bg, padx=14, pady=10)
        bubble.pack(fill=tk.X)

        tk.Frame(bubble, bg=bar_color, width=4).pack(
            side=tk.LEFT, fill=tk.Y, padx=(0, 10))

        tk.Label(
            bubble, text=text, font=self.font_msg,
            bg=bubble_bg, fg=TEXT_DARK,
            wraplength=580, justify=tk.LEFT, anchor="w"
        ).pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.root.after(60, self._scroll_bottom)

    def _scroll_bottom(self):
        self.canvas.update_idletasks()
        self.canvas.yview_moveto(1.0)

    # ── send / receive 

    def _on_send(self):
        msg = self.entry_var.get().strip()
        if not msg:
            self._shake_entry()
            return
        self.entry_var.set("")
        self._add_bubble("You", msg, ACCENT_YELLOW, "right", "👤")
        self.send_btn.config(state=tk.DISABLED)
        threading.Thread(target=self._bot_reply, args=(msg,), daemon=True).start()

    def _bot_reply(self, msg: str):
        for dots in [".", "..", "..."]:
            self.typing_var.set(f"🐍 PyBuddy is thinking{dots}")
            time.sleep(0.28)
        self.typing_var.set("")
        response = get_response(msg)
        self.root.after(0, lambda: self._add_bubble(
            "PyBuddy", response, ACCENT_BLUE, "left", "🐍"))
        self.root.after(0, lambda: self.send_btn.config(state=tk.NORMAL))
        self.root.after(0, self.entry.focus_set)

    def _shake_entry(self):
        x0 = self.entry.winfo_x()
        def shake(n, d):
            if n == 0: return
            self.entry.place(x=x0 + d * 4)
            self.root.after(35, lambda: shake(n - 1, -d))
        shake(6, 1)

    def _on_key(self, event=None):
        if self.entry_var.get():
            self.entry.config(highlightcolor=ACCENT_YELLOW)
        else:
            self.entry.config(highlightcolor=ACCENT_BLUE)

    # ── header pulse animation (alternates yellow ↔ blue) ───────────────────

    def _animate_header(self):
        colors = [ACCENT_YELLOW, "#ffe680", ACCENT_BLUE, "#7ab8e8", ACCENT_YELLOW]
        idx = [0]
        def pulse():
            self.title_lbl.config(fg=colors[idx[0] % len(colors)])
            idx[0] += 1
            self.root.after(950, pulse)
        pulse()

    # ── welcome messages ─────────────────────────────────────────────────────

    def _post_welcome(self):
        msgs = [
            "Welcome to PyBuddy — your Python & CS Fundamentals Tutor! 🐍🎉\nI'm here to help you learn — patiently, clearly, and with a few jokes.",
            "I can teach you:\n  💻 Computer Basics (hardware, software, binary, internet)\n  🐍 Python Language (what it is, why it matters)\n  📦 All Programming Fundamentals (variables → classes)",
            "Type 'help' to see the full menu of topics.\nOr just ask: 'What is Python?' or 'Explain variables' 🎯",
            "No question is too basic here.\nEvery expert started exactly where you are now 😊",
        ]
        for i, m in enumerate(msgs):
            self.root.after(300 + i * 900,
                            lambda msg=m: self._add_bubble(
                                "PyBuddy", msg, ACCENT_BLUE, "left", "🐍"))


# ── entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app  = ChatApp(root)
    root.mainloop()