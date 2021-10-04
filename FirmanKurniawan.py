def kalkulator(pilih, angka1, angka2):
    if(pilih == "1"):
        tambah = angka1 + angka2
        print(tambah)
    elif(pilih == "2"):
        kurang = angka1 - angka2
        print(kurang)
    elif(pilih == "3"):
        kali = angka1 * angka2
        print(kali)
    else:
        bagi = angka1 / angka2
        print(bagi)

print("1.Tambah \n2.Kurang\n3.Kali\n4.Bagi")
kalkulator(input("Masukkan Pilihan (1-4): "),int(input("Masukkan angka pertama: ")),int(input("Masukkan angka kedua: ")))
