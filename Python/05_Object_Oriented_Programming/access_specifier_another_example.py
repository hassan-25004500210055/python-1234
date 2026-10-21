# access specifier another example
class ABC:
    def __init__(self):
        self.first_number=10
        self._b=20
        self.__c=30
    def putData(self):
        print(self.first_number)
        print(self._b)
        print(self.__c)
class XYZ(ABC):
    def showData(self):
        print("A is :",self.first_number)
        print("_B is :",self._b)

x1 = XYZ()
x1.showData()
print(x1.first_number)
print(x1._b)
print(x1.__c)
