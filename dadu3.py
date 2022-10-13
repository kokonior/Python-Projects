# program dua dadu v3 oleh NIM 030

import random
for x in range(1, 21):
    lempar_1 = random.randint(1, 6)
    lempar_2 = random.randint(1, 6)
    lempar_3 = random.randint(1, 6)

    print("Dadu no.1 = {0}" "Dadu no.2 {1} Dadu no.3 {2}".format(
        lempar_1, lempar_2, lempar_3))

    if lempar_1 == 1 and lempar_2 == 1 and lempar_3 == 1:
        print('TRIPLE ONE !!')
    if lempar_1 == 6 and lempar_2 == 6 and lempar_3 == 6:
        print('TRIPLE SIX !!')
    if lempar_1 == lempar_2 or lempar_1 == lempar_3 or lempar_2 == lempar_3:
        print('Double DICE!!')
