import os
import msvcrt as m

def wait():
    m.getch()

print(" - Memanggil Fungsi - ")
def greet():
    print("Charoo~")
greet()

print(" - Arguments - ")
def fungsi(nama_depan):
    print(nama_depan, "Wijaya")
fungsi("Agus")
fungsi("Udin")

print(" - 2 Arguments - ")
def namur(Nama, Umur):
    print("Halo, saya ",Nama,"berumur",Umur," tahun.")
namur("Agus",18)
namur("Udin",19)

print(" - Arbitary Arguments - ")
def kurang(*a):
    print("Hasil dari",a[0], "-", a[1], "adalah" ,a[0]-a[1])
kurang(5,2)
kurang(6,4)

print(" - Keyword Arguments - ")
def nama_anak(anak1,anak2,anak3):
    print("Nama anak ini adalah",anak1)
nama_anak(anak1 = "Udin", anak2="Meguru", anak3="Pari")

print(" - Arbitary Keyword Arguments - ")
def ningen(**jenis):
    print("Dia " + jenis["jenis2"])
ningen(jenis1 = "Binatang", jenis2 = "Manusia")

print(" - Default Parameter Value - ")
def game(fav = "Sumpok"):
    print("Game favorite saya adalah",fav)
game("Aokana")
game("Sanoba Witch")

print(" - Passing a List as an Arguments - ")
def function(bebas):
    for x in bebas:
        print(x)
HP = ["POCO", "ASUS", "OPPO"]
function(HP)

print(" - Return Values - ")
def kali(a):
    return 2 * a
print(kali(2))
print(kali(5))
print(kali(7))

wait()
os.system('cls')

ans=True
while ans:
    print("""
    Menu :
    ------------

    1.Luas Kubus
    2.Vol Kubus
    3.Luas Balok
    0.Exit/Quit
    """)
    ans=input("Apa yang ingin anda pilih? ")
    os.system('cls')
    if ans=="1":
            print("""
               o--------o
              /        /|
             /        / |
            o--------o  |
            |        |  o
            |        | /
            |        |/ 
            o--------o""")
            try:
                s = int(input("Sisi : "))
            except ValueError:
                print("Hanya masukkan angka!")
                wait()
                continue
            rumus = 6 * s * s
            print("Hasil Luas Kubus adalah :",rumus)
            print("\nTekan Enter...")
            wait()
            os.system('cls')
        
    elif ans=="2":
            print("""
               o--------o
              /        /|
             /        / |
            o--------o  |
            |        |  o
            |        | /
            |        |/ 
            o--------o""")
            try:
                s = int(input("Rusuk : "))
            except ValueError:
                print("Hanya masukkan angka!")
                wait()
                continue
            rumus = s * s * s
            print("Hasil Volume Kubus adalah :",rumus)
            print("\nTekan Enter...")
            wait()
            os.system('cls')

    elif ans=="3":
            try:
                p = int(input("Panjang : "))
                l = int(input("Lebar : "))
                t =  int(input("Tinggi : ")) 
            except ValueError:
                print("Hanya masukkan angka!")
                wait()
                continue
            rumus = 2 * (p*l+p*t+l*t)
            print("Hasil Luas Balok adalah :",rumus)
            print("\nTekan Enter...")
            wait()
            os.system('cls')
        
      
    elif ans=="0":
      print("\nGoodbye") 
      ans = None
    else:
      print("\nPilihan Tidak Ada Coba Lagi")
      print("\nTekan Enter...")
      wait()
      os.system('cls')
      ans = True
