# 📁 Topic 2: File Handling in Python

---

## 🎯 Learning Objectives

By the end of this session, you will be able to:

- Understand what file handling is in Python
- Use various file modes: read, write, append, etc.
- Read and write both text and binary files
- Apply context managers (`with` statement)
- Handle file-related exceptions
- Work with file paths and directories
- Use file handling in real-world applications

---

## 📚 What is File Handling?

- File handling in Python allows you to **store**, **read**, and **modify** data stored in files.
- Useful when:
  - Saving data (e.g., logs, user data)
  - Loading configurations
  - Data processing tasks

---

## 🔄 File Modes in Python

| Mode   | Description                                       |
|--------|---------------------------------------------------|
| `'r'`  | Read-only (default); file **must exist**          |
| `'w'`  | Write-only; creates a **new file or overwrites**  |
| `'a'`  | Append; adds content **at the end** of file       |
| `'x'`  | Create new file; **error if file exists**         |
| `'b'`  | Binary mode (used with `rb`, `wb`, etc.)          |
| `'t'`  | Text mode (default)                               |
| `'r+'` | Read and write; file **must exist**               |

---

## 📖 Basic File Operations

### 🔓 Opening a File

```python
file = open("data.txt", "r")  # Opens file in read mode
```

### 📖 Reading from a File

```
 file = open("data.txt", "r")

print(file.read())       # Read entire content
print(file.readline())   # Read one line
print(file.readlines())  # Read all lines as a list

file.close()

```
- 💡 Tip: Use .strip() to clean \n from lines when reading line-by-line.

### ✍️ Writing to a File
```
file = open("output.txt", "w")
file.write("Hello, Python!\n")
file.write("Overwriting existing content.")
file.close()

```
### ➕ Appending to a File
```
file = open("output.txt", "a")
file.write("\nThis line is appended.")
file.close()
```
### ✅ Using with open() — Context Manager
```
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
```
### ✅ Why use with?
- Automatically closes the file after the block

- Cleaner and safer (especially in exception handling)

## 🧰 Common File Methods

| Method             | Description                              |
|--------------------|------------------------------------------|
| `read()`           | Reads entire file content                |
| `readline()`       | Reads a single line                      |
| `readlines()`      | Returns a list of all lines              |
| `write(string)`    | Writes a string to the file              |
| `writelines(list)` | Writes a list of strings to the file     |
| `close()`          | Closes the file                          |
| `seek(pos)`        | Moves file pointer to specified position |
| `tell()`           | Returns current file pointer position    |

### 🛠️ File Path & Directory Operations
```
import os

# Get current working directory
print(os.getcwd())

# Check if a file exists
print(os.path.exists("data.txt"))

# Create a new directory
os.mkdir("new_folder")
```
### 🔐 Exception Handling in File Operations
```
try:
    with open("file.txt", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("Error: File not found.")
except IOError:
    print("Error: Cannot read the file.")
```
#### 🧠 Text Files vs Binary Files
- Text Files	  Binary Files
Human-readable	   Not human-readable (e.g., images)
Use 'r', 'w', 'a' 	Use 'rb', 'wb', 'ab'
Stores plain text	Stores bytes

#### 🧪 Example: Writing Binary File
```
with open("image.jpg", "rb") as file:
    data = file.read()

with open("copy.jpg", "wb") as file:
    file.write(data)
```
#### 💼 Real-World Use Cases
- Logging user activity or system events

- Saving chatbot conversations or game scores

- Reading configuration files for apps

- Exporting reports or scraped web data

- Temporary file storage in web apps

#### 🧩 Challenge Activity
🧠 Task: Create a program that does the following:

Takes user input (name and score)

Saves it to a file named scores.txt

Reads and displays all scores from the file

```
# Writing input
with open("scores.txt", "a") as f:
    name = input("Enter your name: ")
    score = input("Enter your score: ")
    f.write(f"{name} - {score}\n")

# Reading scores
with open("scores.txt", "r") as f:
    print("\nAll Scores:")
    print(f.read())
```

#### ✅ Quick Recap

- Use open(filename, mode) for file operations

- Prefer with open(...) to manage file lifecycle

- Understand text vs binary modes

- Handle exceptions using try-except

- Real-world usage includes logs, configs, and storage

