#inner funct
def funct():
    print("first function")
    def funct1():
        print("1st child")
    def funct2():
        print("1st child")
    def funct3():
        print("1st child")
    funct1()
    funct2()
    funct3()
funct()