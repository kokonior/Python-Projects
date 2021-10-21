#Febrian Ardi Pangestu 21060119130125
#program parkir
def resetbiayaparkir():
    global biayaparkir
    biayaparkir=0
def punyavoc():
    global vocnya,punyavocnya
    vocnya=str(input("Punya voc? (ya/tidak): "))
    if vocnya == "ya":
        punyavocnya = 1
    else:
        punyavocnya = 0
def inputjam():
    global jammasuk,jamkeluar,biayahari,biayaparkir,hitungjam
    print("input jam dengan format 24jam, hanya 2 digit jam pertama")
    jammasuk=int(input("Jam masuk:"))
    jamkeluar=int(input("Jam keluar:"))
    if (jamkeluar<jammasuk):
        jamkeluar=jamkeluar+24
    else:
        jamkeluar=jamkeluar
    if (jamkeluar-jammasuk)>12:
        punyavoc()
        if punyavocnya==1:
            biayaparkir=biayaparkir+10000
        else:
            biayaparkir=biayaparkir+20000
    else:
        hitungjam=jamkeluar-jammasuk-2
        if hitungjam<0:
            hitungjam=0
        else:
            hitungjam=hitungjam
        biayaparkir=2000+1000*(hitungjam)
    print("Parkir salama:",(jamkeluar-jammasuk),"jam")
    print("Biaya parkir:",biayaparkir)
    print("")
def fungsiutama():
    resetbiayaparkir()
    inputjam()
    resetbiayaparkir()
    fungsiutama()
fungsiutama()
        
'''
output
input jam dengan format 24jam, hanya 2 digit jam pertama
Jam masuk:1
Jam keluar:2
Parkir salama: 1 jam
Biaya parkir: 2000

input jam dengan format 24jam, hanya 2 digit jam pertama
Jam masuk:1
Jam keluar:3
Parkir salama: 2 jam
Biaya parkir: 2000

input jam dengan format 24jam, hanya 2 digit jam pertama
Jam masuk:1
Jam keluar:4
Parkir salama: 3 jam
Biaya parkir: 3000

input jam dengan format 24jam, hanya 2 digit jam pertama
Jam masuk:1
Jam keluar:23
Punya voc? (ya/tidak): ya
Parkir salama: 22 jam
Biaya parkir: 10000

input jam dengan format 24jam, hanya 2 digit jam pertama
Jam masuk:1
Jam keluar:23
Punya voc? (ya/tidak): tidak
Parkir salama: 22 jam
Biaya parkir: 20000

input jam dengan format 24jam, hanya 2 digit jam pertama
Jam masuk:23
Jam keluar:1
Parkir salama: 2 jam
Biaya parkir: 2000

input jam dengan format 24jam, hanya 2 digit jam pertama
Jam masuk:24
Jam keluar:1
Parkir salama: 1 jam
Biaya parkir: 2000

input jam dengan format 24jam, hanya 2 digit jam pertama
Jam masuk:24
Jam keluar:3
Parkir salama: 3 jam
Biaya parkir: 3000

input jam dengan format 24jam, hanya 2 digit jam pertama
Jam masuk:24
Jam keluar:14
Punya voc? (ya/tidak): ya
Parkir salama: 14 jam
Biaya parkir: 10000

input jam dengan format 24jam, hanya 2 digit jam pertama
Jam masuk:24
Jam keluar:14
Punya voc? (ya/tidak): tidak
Parkir salama: 14 jam
Biaya parkir: 20000
'''
