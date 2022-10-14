def get_winner(p1, p2):
    if p1 == p2:
        return "It's a tie!"
    elif p1 == "rock":
        if p2 == "scissors":
            return "First player wins!"
        else:
            return "Second Player wins!"
    elif p1 == "scissors":
        if p2 == "paper":
            return "First player win!"
        else:
            return "Second player wins!"
    elif p1 == "paper":
        if p2 == "rock":
            return "First player wins!"
        else:
            return "Second player win!"
    else:
        return "Invalid input!"


player1 = input("First player: rock, paper or scissors: ")
player2 = input("Second Player: rock, paper or scissors: ")

print(get_winner(player1, player2))
