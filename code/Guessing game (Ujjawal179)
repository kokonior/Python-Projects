 print("GUESSING GAME")

while(True):
    x= str(input("Shall we start the game: \n"))
    y=x.lower()
    import random
    n= random.randint(1,30)
    if y=="yes":
        name = str(input("Enter your name:"))
        print("Hello " + name + ",\n In this game I will choose a number between 1 and 30 and you have to guess it")
        a1=int(input("Your guess is:"))
        print("Great your guess is right \n Wow, you won ;-)")  if a1==n else print("Oh no, you must try again \n Try again you have 4 more chances to guess")
        if a1==n:
            print("Thanks for playing")
        else:
            a2=int(input("Your second guess is:"))
            print("Great your guess is right \n Wow, you won ;-)") if a2==n else print("Oh no, you was close \n Try again you have 3 more chances to guess")
            if a2==n:
                  print("Thanks for playing")
            else:
               a3= int(input("Your third guess is:"))
               print("Great your guess is right \n Wow, you won ;-)") if a3==n else print("Oh no, you was too close \n Try again you have 2 more chances to guess")
               if a3==n:
                      print("Thanks for playing")
               else:
                      a4= int(input("Your fourth guess is:"))
                      print("Great your guess is right \n Wow, you won ;-)") if a4==n else print("Oh no, you was almost there \n Try again you have 1 more last chance to guess")
                      if a4==n:
                         print("Thanks for playing")
                      else:
                            a5= int(input("Your last guess is:"))
                            print("Great your guess is right \n Wow, you won ;-)") if a5==n else print(f"Better luck next time and answer was {n}. \n GAME OVER")
    else:
       print("Hope to see you next time!")
