# program dua dadu v2 oleh NIM 030

import random
while True:
    lempar_1 = random.randint(1, 6)
    lempar_2 = random.randint(1, 6)
    print("Dadu no.1 = {}".format(lempar_1, lempar_2))
    print("Dadu no.2 = {}".format(lempar_1, lempar_2))
    if lempar_1 == 6 and lempar_2 == 6:
        break
print('DOUBLE SIX !!!!!')
