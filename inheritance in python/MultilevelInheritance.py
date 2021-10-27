class Student:
    def __init__(self, a):
        self.__rollNumber = a

    def putNumber(self):
        return self.__rollNumber


class Test(Student):
    def __init__(self, a, b, c):
        super().__init__(a)
        self.sub1 = b
        self.sub2 = c

    def putMarks(self):
        return self.sub1, self.sub2


class Result(Test):
    def display(self):
        total = self.sub2+self.sub1
        x, y = self.putMarks()
        print(f"Roll Number = {self.putNumber()} ")
        print(f"Sub 1 = {x} ")
        print(f"Sub 2 = {y} ")
        print(f"Total = {total} ")


print('======= Nomor 2 =======')
soal2 = Result(12, 4, 3)
soal2.display()
