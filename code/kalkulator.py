# kalkulator sederhana

print("\n[-]KALKULATOR SEDERHANA[-]")
print("\n1. Perkalian\n2. Pembagian\n3. Pertambahan\n4. Pengurangan")
pilih = int(input("\nMau apa ? => "))
if pilih == 1:
	x = int(input("\nMasukkan angka pertama => "))
	y = int(input("Masukkan angka kedua => "))
	print("Hasil dari Perkalian",x,"dan",y,"=> {:,}".format(x * y))
elif pilih == 2:
	x = int(input("Masukkan angka pertama => "))
	y = int(input("Masukkan angka kedua => "))
	print("Hasil dari Pembagian",x,"dan",y,"=> {:,}".format(x  / y))
elif pilih == 3:
	x = int(input("Masukkan angka pertama => "))
	y = int(input("Masukkan angka kedua => "))
	print("Hasil dari Pertambahan",x,"dan",y,"=> {:,}".format(x  + y))
elif pilih == 4:
	x = int(input("Masukkan angka pertama => "))
	y = int(input("Masukkan angka kedua => "))
	print("Hasil dari Pengurangan",x,"dan",y,"=> {:,}".format(x  - y))
else:
	print("PILIHAN TIDAK TERSEDIA")