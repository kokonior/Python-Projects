import math
# method overloading in python example

class sumBilangan():
    def jumlah(self, a=None, b=None, c=None, d=None):
        if a != None and b != None and c != None and d != None:
            print("Penjumlahan a+b+c+d")
            print("a = ", a)
            print("b = ", b)
            print("c = ", c)
            print("d = ", d)
            sum = a+b+c+d
            print("Hasil penjumlahan")
            print(">", a, "+", b, "+", c, "+", d, " = ", sum, "\n")
            return (sum)
        elif a != None and b != None and c != None:
            print("Penjumlahan a+b+c")
            print("a = ", a)
            print("b = ", b)
            print("c = ", c)
            sum = a+b+c
            print("Hasil Penjumlahan")
            print(">", a, "+", b, "+", c, " = ", sum, "\n")
            return (sum)
        elif a != None and b != None:
            print("Penjumlahan a+b")
            print("a = ", a)
            print("b = ", b)
            sum = a+b
            print("Hasil Penjumlahan")
            print(">", a, "+", b, " = ", sum, "\n")
            return (sum)
        else:
            print("Penjumlahan a")
            print("a = ", a)
            sum = ("> Tidak dapat menghitung penjumlahan\n")
            print("Hasil Penjumlahan")
            return (sum)


class bungaMajemuk():
    def bunga(self, mo=None, bm=None, bl=None, t=None):
        if mo != None and bm != None and bl != None:
            Mt = "{:.2f}".format(float(mo*(1+bm)**bl))
            print("Modal awal = ", mo)
            print("Bunga = ", bm)
            print("Bulan = ", bl, " bulan")
            print("Bunga Majemuk = ", Mt, "\n")
        else:
            Mt = ("Tidak dapat menghitung bunga majemuk")
            print("Modal awal = ", mo)
            print("Bunga = ", bm)
            print("Bulan = ", bl, " bulan")
            print(Mt, "\n")
            return Mt


class volSilinder():
    def silinder(self, r=None, t=None):
        if r != None and t != None:
            Vs = "{:.2f}".format(float(math.pi*(r**2)*t))
            print("Jari-jari = ", r)
            print("Tinggi = ", t)
            print("Volume Silinder = ", Vs, "\n")
            return Vs
        else:
            Vs = ("Tidak dapat menghitung volume silinder")
            print("Jari-jari = ", r)
            print("Tinggi = ", t)
            print(Vs, "\n")


class volBalok():
    def balok(self, p=None, l=None, t=None):
        if p != None and l != None and t != None:
            Vb = "{:.2f}".format(float(p*l*t))
            print("Panjang = ", p)
            print("Lebar = ", l)
            print("Tinggi = ", t)
            print("Volume Balok = ", Vb, "\n")
            return Vb
        else:
            Vb = ("Tidak dapat menghitung volume balok")
            print("Panjang = ", p)
            print("Lebar = ", l)
            print("Tinggi = ", t)
            print(Vb, "\n")


print("No. 1 Penjumlahan")
b = sumBilangan()
b.jumlah(71, 45, 1, 22)
b.jumlah(7, 11, 43)
b.jumlah(10, 21)
f = b.jumlah(1)
print(f)
print("\n")


print("No. 2 Bunga Majemuk")
bm = bungaMajemuk()
bm.bunga(1000000, 0.05, 12)
bm.bunga(2500000, 0.03, 5)
bm.bunga(2000000, 0.08)
print("\n")

print("No. 3 Volume Silinder")
vs = volSilinder()
vs.silinder(3, 7)
vs.silinder(4)
print("\n")


print("No. 4 Volume Balok")
vb = volBalok()
vb.balok(2, 9, 4)
vb.balok(5, 6)
print("\n")
