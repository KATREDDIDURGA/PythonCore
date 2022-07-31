'''class decorators
https://www.youtube.com/watch?v=WGJJIrtnfpk?t=05h00m00s


'''

class Square:
    def __init__(self,side):
        self.side = side
    @property
    def side(self):
        return self.__side
    @side.setter
    def side(self,value):
        if value>=0:
            self.__side = value
        else:
            print("Error")
    @property
    def area(self):
        return self.__side**2
    @classmethod
    def unit_square(cls):
        return cls(1)
s = Square(5)
print(s.side)
print(s.area)

