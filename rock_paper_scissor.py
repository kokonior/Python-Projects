# create a list of play options
t = ["Rock", "Paper", "Scissors"]

# assign a random play to the computer
computer = t[randint(0, 2)]

# set player to False
player = False

while player is False:
    # set player to True
    speak("Choose rock, paper or scissors")
    player_choice = takecommand()
    if 'rock' in player_choice:
        player = "Rock"

    elif 'paper' in player_choice:
        player = "Paper"

    elif 'scissors' in player_choice:
        player = "Scissors"

    else:
        speak("That's not a valid play. Check your spelling!")

    if player == computer:
        speak("It's a tie, you chose" + player + "and Computer chose" + computer)

    elif player == "Rock":
        if computer == "Paper":
            speak("You lose!" + computer + "covers" + player)
        else:
            speak("You win!" + player + "smashes" + computer)
    elif player == "Paper":
        if computer == "Scissors":
            speak("You lose!" + computer + computer + "cut" + player)
        else:
            speak("You win!" + player + "covers" + computer)
    elif player == "Scissors":
        if computer == "Rock":
            speak("You lose..." + computer + "smashes" + player)
        else:
            speak("You win!" + player + "cut" + computer)

    # player was set to True, but we want it to be False so the loop continues
    speak("Do you wanna play again")
    play_again = takecommand()
    if 'yes' in play_again or 'ya' in play_again:
        play_again = False

    else:
        play_again = True
        speak("Exited Rock Paper scissors")
    player = play_again
    computer = t[randint(0, 2)]
