class B:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def showA(self):
        print(self.__a)

    def showB(self):
        print(self.__b)


class D(B):
    def mul(self):
        c = self.getB()*self.getA()
        return c

    def dev(self):
        d = self.getB()/self.getA()
        return d

    def display(self, w, x, y, z):
        print(f"A = {self.getA()} ")
        print(f"B = {self.getB()} ")
        print(f"C = {self.mul()} ")
        print(f"D = {self.dev()} ")


print('======= Nomor 1 =======')
soal1 = D(10, 13)
print(f"A = {soal1.getA()}")
print(f"B = {soal1.getB()}")
print(f"C = {soal1.mul()}")
print(f"D = {soal1.dev()}")
