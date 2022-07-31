f = open("C:/Users/kasi/PycharmProjects/pythonProjectTest/File Handling/testfile.txt", "r")
for line in f:
    print(f.readlines())
f.close()

print("*****************************")

f = open("C:/Users/kasi/PycharmProjects/pythonProjectTest/File Handling/testfile.txt", "r")
for line in f:
    print(f.readline())
f.close()

