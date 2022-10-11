## Pythagoras for Triangle
## Find A, B, and C

from cmath import sqrt
import math
from re import A


def A_Triangle():

    angka1 = float(input("Insert number C -> "))
    angka2 = float(input("Insert number B -> "))

    akar = float(math.sqrt(angka1*angka1 - angka2*angka2))
    bulat = round(akar, 2)
    print("Result of A is : "+str(bulat))

def B_Triangle():

    angka1 = float(input("Insert number C -> "))
    angka2 = float(input("Insert number A -> "))

    akar = float(math.sqrt(angka1*angka1 - angka2*angka2))
    bulat = round(akar, 2)
    print("Result of B is : "+str(bulat))

def C_Triangle():

    angka1 = float(input("Insert number A -> "))
    angka2 = float(input("Insert number B -> "))

    akar = float(math.sqrt(angka1*angka1 + angka2*angka2))
    bulat = round(akar, 2)
    print("Result of C is : "+str(bulat))

def banner():

    print("""

    Simple Script to Calculate Pythagoras on Triangle

    [1]. Find A
    [2]. Find B
    [3]. Find C

    """)

if __name__ == "__main__":
    banner()
    pilih = input("Your option ? ")

    if pilih == "1":
        A_Triangle()
    elif pilih == "2":
        B_Triangle()
    elif pilih == "3":
        C_Triangle()
    else:
        print("No Options!")

