import math


class Shape:
    def __init__(self, a):
        self.__name = a

    def getName(self):
        return self.__name

    def calculateArea(self):
        pass


class Circle(Shape):
    def __init__(self, a, r):
        super().__init__(a=a)
        self.radius = r

    def calculateArea(self):
        res = math.pow(self.radius, 2) * math.pi
        return res


class Square(Shape):
    def __init__(self, a, s):
        super().__init__(a=a)
        self.side = s

    def calculateArea(self):
        res = math.pow(self.side, 2)
        return res


print('======= Nomor 3 =======')
soal3 = Circle("Lingkaran", 10)
print(f"NAMA SHAPE = {soal3.getName()}")
print(f"Luas Lingkaran = {soal3.calculateArea()}")
soal3_2 = Square("Persegi", 10)
print(f"NAMA SHAPE = {soal3_2.getName()}")
print(f"Luas Persegi = {soal3_2.calculateArea()}")
