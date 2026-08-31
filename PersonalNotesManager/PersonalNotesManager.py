# File Handling Demonstration in Python
# File used: notes.txt

# --------------------------------------------------
# 1. Creating the file and writing at least 10 lines
# Mode: "w" (write)
# --------------------------------------------------

file = open("notes.txt", "w")

file.write("Note 1: Python is easy to learn.\n")
file.write("Note 2: Files can store data permanently.\n")
file.write("Note 3: The open() function is used to open files.\n")
file.write("Note 4: The read() function reads file contents.\n")
file.write("Note 5: The write() function writes data to a file.\n")
file.write("Note 6: The append mode adds data to an existing file.\n")
file.write("Note 7: The close() function closes a file.\n")
file.write("Note 8: readline() reads one line at a time.\n")
file.write("Note 9: readlines() reads all lines into a list.\n")
file.write("Note 10: Python supports different file modes.\n")

file.close()

print("File created and 10 lines written successfully.")


# --------------------------------------------------
# 2. Reading the entire file
# Mode: "r" (read)
# --------------------------------------------------

file = open("notes.txt", "r")

content = file.read()

print("\n--- Entire File ---")
print(content)

file.close()


# --------------------------------------------------
# 3. Reading a specific number of characters
# --------------------------------------------------

file = open("notes.txt", "r")

characters = file.read(20)

print("--- First 20 Characters ---")
print(characters)

file.close()


# --------------------------------------------------
# 4. Using readline()
# Reads one line at a time
# --------------------------------------------------

file = open("notes.txt", "r")

first_line = file.readline()

print("\n--- Using readline() ---")
print(first_line)

file.close()


# --------------------------------------------------
# 5. Using readlines()
# Reads all lines and stores them in a list
# --------------------------------------------------

file = open("notes.txt", "r")

lines = file.readlines()

print("--- Using readlines() ---")

for line in lines:
    print(line, end="")

file.close()


# --------------------------------------------------
# 6. Appending additional notes
# Mode: "a" (append)
# --------------------------------------------------

file = open("notes.txt", "a")

file.write("Note 11: Always remember to close files.\n")
file.write("Note 12: The with open() statement closes files automatically.\n")

file.close()

print("\n\nAdditional notes appended successfully.")


# --------------------------------------------------
# 7. Reopening the file and displaying updated contents
# --------------------------------------------------

file = open("notes.txt", "r")

updated_content = file.read()

print("\n--- Updated File Contents ---")
print(updated_content)

file.close()


# --------------------------------------------------
# 8. Demonstrating with open()
# --------------------------------------------------

print("--- Demonstrating with open() ---")

with open("notes.txt", "r") as file:
    content = file.read()
    print(content)

# The file is automatically closed after the with block.

### File modes demonstrated

# * **`"r"` — Read mode:** Opens an existing file for reading.
# * **`"w"` — Write mode:** Creates a new file or replaces the contents of an existing file.
# * **`"a"` — Append mode:** Adds new content to the end of an existing file.

### Why is `with open()` preferred?

# Normally, when using `open()`, you have to remember to call `close()`:

# file = open("notes.txt", "r")
# data = file.read()
# file.close()

# With `with open()`, Python automatically closes the file when the block finishes:

# with open("notes.txt", "r") as file:
#     data = file.read()

# This is preferred because it is **safer, cleaner, and easier to maintain**. Even if an error occurs inside the `with` block, Python will still close the file automatically.

# **Note:** `read()` is used to read the entire file or a specified number of characters, while `readline()` reads one line and `readlines()` returns the remaining lines as a list.
