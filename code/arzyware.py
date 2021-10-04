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

print(" - The Pass Statement - ")
def pro():
    pass
    
