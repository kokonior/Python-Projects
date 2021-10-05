#program to calculate the area of plane figure
print("Program Menghitung Luas Bangun Datar (dalam cm)")
print("1.Persegi")
print("2.Persegi Panjang")
print("3.Segitiga")
print("4.Layang-Layang atau Belah Ketupat")
print("5.Trapesium")
#input name of plane figure
bangundatar = input("Masukkan nama bangun datar yang ingin dihitung :")
#process
if bangundatar == "1":
    sisi = float(input("Masukkan sisinya :"))
    luas = sisi * sisi
#output of area
    print("Luas bangunan tersebut adalah " + str(luas))
else:
    if bangundatar == "2":
        panjang = float(input("Masukkan panjangnya :"))
        lebar = int(input("Masukkan lebarnya :"))
        luas = panjang * lebar
    else:
        if bangundatar == "3":
            alas = float(input("Masukkan alas :"))
            tinggi = float(input("Masukkan tinggi :"))
            luas = float(1) / 2 * alas * tinggi
        else:
            if bangundatar == "4":
                alas = float(input("Masukkan alas :"))
                tinggi = float(input("Masukkan tinggi :"))
                luas = alas * tinggi
            else:
                if bangundatar == "5":
                    d1 = float(input("Masukkan luas d1 :"))
                    d2 = float(input("Masukkan luas d2 :"))
                    luas = d1 * d2 / 2
                else:
                    if bangundatar == "6":
                        sisialas = float(input(""))
                        sisibawah = float(input())
                        tinggi = float(input())
                        luas = (sisialas + sisibawah) * (tinggi / 2)
                    else:
                        print("ERROR, MASUKKAN BANGUN DATAR YANG VALID")
#output of area
    print("Luas bangunan tersebut adalah : " + str(luas) + " cm" )
