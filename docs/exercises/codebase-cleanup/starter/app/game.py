



from random import choice

#
# USER SELECTION
#

u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
print("USER CHOICE:", u)
if u not in ["rock", "paper", "scissors"]:
    print("OOPS, TRY AGAIN")
    exit()

#
# COMPUTER SELECTION
#

c = choice(["rock", "paper", "scissors"])
print("COMPUTER CHOICE:", c)

#
# DETERMINATION OF WINNER
#

if u == "rock" and c == "rock":
    print("It's a tie!")
elif u == "rock" and c == "paper":
    print("The computer wins")
elif u == "rock" and c == "scissors":
    print("The user wins")

elif u == "paper" and c == "rock":
    print("The computer wins")
elif u == "paper" and c == "paper":
    print("It's a tie!")
elif u == "paper" and c == "scissors":
    print("The user wins")

elif u == "scissors" and c == "rock":
    print("The computer wins")
elif u == "scissors" and c == "paper":
    print("The user wins")
elif u == "scissors" and c == "scissors":
    print("It's a tie!")
