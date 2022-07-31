import os

if os.path.exists("C:/Users/kasi/PycharmProjects/pythonProjectTest/File Handling/testfile1.txt"):
    os.remove("C:/Users/kasi/PycharmProjects/pythonProjectTest/File Handling/testfile1.txt")
else:
    print("file doesn't exist")
