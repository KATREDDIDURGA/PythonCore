import os
file = open("C:/Users/kasi/PycharmProjects/pythonProjectTest/File Handling/testfile.txt",'w')
file.close()
import os
file = open("C:/Users/kasi/PycharmProjects/pythonProjectTest/File Handling/testfile.txt",'r')
print(file.read())
file.close()

f = open("C:/Users/kasi/PycharmProjects/pythonProjectTest/File Handling/testfile.txt", "r")
print(f.read())
f.close()

f = open("C:/Users/kasi/PycharmProjects/pythonProjectTest/File Handling/testfile.txt", "r")
print(f.read(5))
f.close()



