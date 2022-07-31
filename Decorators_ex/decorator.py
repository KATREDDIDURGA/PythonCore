def function1(function):
    def wrapper():
        print("hello")
        function()
        print("welocme")
    return wrapper
def function2():
    print("hgsagd")
function2 = function1(function2)
function2()

print("********************")

@function1
def function2():
    print("python")
function2()

