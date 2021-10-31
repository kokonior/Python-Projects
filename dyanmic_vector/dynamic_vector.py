class Vektor:
    def __init__(self, *args):
        self.data = list(args)

    def jumlah2Vektor(self, a=None):
        if a != None:
            res = []
            for i in range(len(self.data)):
                tmp = a.data[i]+self.data[i]
                res.append(tmp)
            return res
        else:
            res = []
            for i in range(len(self.data)):
                tmp = self.data[i]+self.data[i]
                res.append(tmp)
            return res

    def selisih2Vektor(self, a=None):
        if a != None:
            res = []
            for i in range(len(self.data)):
                tmp = a.data[i]-self.data[i]
                res.append(tmp)
            return res
        else:
            res = []
            for i in range(len(self.data)):
                tmp = self.data[i]-self.data[i]
                res.append(tmp)
            return res

    def tampilVektor(self):
        return self.data


v1 = Vektor(3, 2, 1, 0)
v2 = Vektor(1, 3, 5, 7)
print(f"Vektor 1 = {v1.tampilVektor()}")
print(f"Vektor 2 = {v2.tampilVektor()}")
print(f"Jumlah Vektor 1 dan 2 = {v1.jumlah2Vektor(v2)}")
print(f"Jumlah Vektor 1 dan Vektor 1 = {v1.jumlah2Vektor()}")
print(f"Selisih Vektor 1 dan Vektor 2 = {v1.selisih2Vektor(v2)}")
print(f"Selisih Vektor 1 dan Vektor 1 = {v1.selisih2Vektor()}")
