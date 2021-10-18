#import module
import random, os, re

#clear console
os.system("cls")

def randomAngka(x, y):
    '''
    Fungsi untuk merandom angka
    '''
    angka = random.randint(x, y)
    return angka

print("=======================================")
print("===== Selamat datang " + os.getlogin() + " =====")
print("===== coba tebak angka dari 11-20 =====")
print("=======================================\n")

print(randomAngka.__doc__)

#inisiasi nomor & counter
nomor = randomAngka(11, 20)
counter = 0

for kesempatan in range(3):
    #increment counter
    counter += 1
    
    #input user with validation
    while(True):
        userInput = int(input("Masukkan angka 11-20: "))
        if userInput < 11 or userInput > 20:
            print("*Angka harus diantara 11-20\n")
        else:
            break
        
    #statement tebakan
    if(userInput == nomor):
        print("Angka yang Anda masukkan BENAR!!\n")
        break
    elif counter == 3:
        print("Maaf, kesempatan kamu sudah habis. Jawabannya adalah", nomor)
        break
    else:
        print("Angka yang Anda masukkan SALAH!!\n")
        continue