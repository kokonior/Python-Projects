print ("Welcome to DICE ROLL")


import random



while True:
    roll = input("Press y to roll dice:")
    if roll == "n":
        break

    print("The dice is rolling...")
    num = random.randint(1,6)
    if num == 1:
        print("|----------|")
        print("|          |")
        print("|     0    |")
        print("|          |")
        print("|----------|")
        print("You got 1")

    if num == 2:
        print("|----------|")
        print("|   0      |")
        print("|          |")
        print("|       0  |")
        print("|----------|")
        print("You got 2")

    if num == 3:
        print("|----------|")
        print("|          |")
        print("|  0  0  0 |")
        print("|          |")
        print("|----------|")
        print("You got 3")
    
    if num == 4:
        print("|----------|")
        print("|  0     0 |")
        print("|          |")
        print("|  0     0 |")
        print("|----------|")
        print("You got 4")

    if num == 5:
        print("|----------|")
        print("| 0     0  |")
        print("|    0     |")
        print("| 0     0  |")
        print("|----------|")
        print("You got 5")

    if num == 6:
        print("|----------|")
        print("|  0     0 |")
        print("|  0     0 |")
        print("|  0     0 |")
        print("|----------|")
        print("You got 6")



        
    


    


        
        




