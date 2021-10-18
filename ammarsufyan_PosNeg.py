import os
import re
os.system("cls") 

print("Selamat datang " + os.getlogin() + "\n")

while(True):
    x = input("Masukkan Angka: ")
    if(re.match('^-?[0-9]+$', str(x))):
        x = int(x)
        break
    else:
        print("\n!!!Masukkan Kembali dengan Benar!!!")

if x > 0:
    print(x, "adalah bilangan positif")
elif x is 0:
    print(x, "adalah bilangan netral")
else:
    print(x, "adalah bilangan negatif")