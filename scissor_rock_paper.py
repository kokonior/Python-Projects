#Program Scissor,rock,paper game"

from random import randint

print("Scissor,Rock,Paper game")

#definition of variable hand
h = ["scissor", "rock", "paper"]
#assign a random play for computer
comp = h[randint(0,2)]
#set player to false
player = False

while player == False:
#set player to true
	  player = input("scissor, rock, or paper?")
	  if player == comp:
	  	print("Draw")
	  elif player == "scissor":
	  	if comp == "rock":
	  		print("You lose")
	  	else:
	  		print("You win")
	  elif player == "scissor":
	  	if comp == "paper":
	  		print("You win")
	  	else:
	  		print("You lose")
	  elif player == "rock":
	  	if comp == "paper":
	  		print("You lose")
	  	else:
	  		print("You win")
	  else:
	  	print("Inputan tidak valid")

#set player to false from true, to do a loop continous
	  player = False
	  comp = h[randint(0,2)]