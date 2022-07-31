def function1(function):
    def wrapper(*args,**kwargs):
        print("hjksfh")
        function(*args,**kwargs)
        print("wek")
    return wrapper
@function1
def function2(name):
    print(f"{name}")
function2("durga")
