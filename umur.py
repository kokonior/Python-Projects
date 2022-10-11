thnkelahiran = int(input("Masukan tahun kelahiran anda :"))
umur = ""
thnsekarang = 2022 

umur = thnsekarang - thnkelahiran

print("Sekarang umur anda " + str(umur))

if umur <= 18:
    print("Anda masih dibawah umur.")
else:
    print("Anda Sudah dewasa!")
