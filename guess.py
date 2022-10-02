answer = int(input("Enter the number in your mind :"))
guess = int(input("Guess a number between 1 and 10 :"))
if guess > answer :
    print("please guess lower number")
    guess = int(input("Guess another number :"))
    if guess == answer :
        print("You guessed correct number")
    else :
        print("You have guessed incorrectly")
elif guess < answer :
    print("please guess higher number")
    guess = int(input("Guess another number :"))
    if guess == answer :
        print("You guessed correct number")
    else :
        print("You have guessed incorrectly")
else :
    print("You guessed correct number")
