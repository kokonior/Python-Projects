# Gambling game!

import random

while(True):
    # Intoduction
    print("Welcome to virtual casino!")
    userName = input("Enter your name to continue: ").capitalize()
    depositAmount = int(input(f"{userName}, enter amount to deposit for playing: $"))
    input("Press any key to continue...\n")

    #Winning number
    winningNum = random.randint(1,10)

    # Rules of game!
    print("RULES!\n")
    print("Rule 1: You have to choose any number between 1 to 10.")
    print("Rule 2: If you choose the right number, you will get 10x the money you bet.")
    print("Rule 3: If you choose the wrong number, you will loose the amount you bet.\n")

    # Start of the game!
    print("Your current balance is $", depositAmount)
    betMoney = int(input("Choose amount of money to bet: $"))
    if betMoney > depositAmount:
        raise Exception("Error! You don't have enough balance!")

    userNum = int(input("Choose an number between 1 and 10: "))

    if userNum == winningNum:
        winAmount = betMoney * 10
        updatedMoney = depositAmount + winAmount
        print("Congratulations! You have chosen the right number!")
        print(f"You won {winAmount}$")
        print(f"{userName}, your balance is now ${updatedMoney}")

    elif userNum != winningNum:
        lostAmount = depositAmount - betMoney
        print(f"Bad luck! You lost ${betMoney}")
        print(f"The winning number was {winningNum}")
        print(f"{userName}, your balance is now ${lostAmount}")
    
    playAgain = input("Do you want to play again? y/n: ")
    if playAgain == 'y' or playAgain == 'yes':
        continue
    else:
        print("Thanks for playing our game.")
        break
