import random

plays = ["Rock", "Paper", "Scissors"]
#ASCII art, kuddos to wynand1004 putting this on github for public use: https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe
ascii_art = {
    "rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    "paper": """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    "scissors": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}


selection = int(input("\nHow many rounds do you want to play? Enter a number: "))
print()
player_1_plays = [None] * selection
computer_plays = [random.randint(0, 2) for _ in range(selection)]
score = [0, 0]

def userGameChoice(input, i):
    match(input.lower()):
        case("rock"):
            player_1_plays[i] = 0
            return("Player picks rock!")
        case("1"):
            player_1_plays[i] = 0
            return("Player picks rock!")
        case("paper"):
            player_1_plays[i] = 1
            return("Player picks paper!")
        case("2"):
            player_1_plays[i] = 1
            return("Player picks paper!")
        case("scissors"): 
            player_1_plays[i] = 2
            return("Player picks scissors!")
        case("3"):
            player_1_plays[i] = 2
            return("Player picks scissors!")
        case _:
            return("Invalid input.... Type the choice or type the number of the choice.")


for i in range(selection):
    print(f"******* Round {i+1} *******")

    while (True):
        choose = str(input("What will you play? 1. Rock, 2. Paper, or 3. Scissors? "))
        answer = userGameChoice(choose, i)
        print(answer+"\n")
        if(answer.startswith("Invalid")):
            continue
        else:
            break

    print(f"Player 1: {plays[player_1_plays[i]]} \n{ascii_art[(plays[player_1_plays[i]].lower())]}")
    print(f"Computer: {plays[computer_plays[i]]} \n{ascii_art[(plays[computer_plays[i]].lower())]}")
    if (player_1_plays[i] == 0):
        if(computer_plays[i] == 1):
            print("Computer wins, +1 Point")
            score[1] += 1
        elif(computer_plays[i] == 0):
            print("Tie - No Points")
        else:
            print("Player 1 win +1 Point")
            score[0] += 1
    if (player_1_plays[i] == 1):
        if(computer_plays[i] == 2):
            print("Computer wins, +1 Point")
            score[1] += 1
        elif(computer_plays[i] == 1):
            print("Tie - No Points")
        else:
            print("Player 1 win +1 Point")
            score[0] += 1
    if (player_1_plays[i] == 2):
        if(computer_plays[i] == 0):
            print("Computer wins, +1 Point")
            score[1] += 1
        elif(computer_plays[i] == 2):
            print("Tie - No Points")
        else:
            print("Player 1 win +1 Point")
            score[0] += 1
            
    if(i <= selection-2):
        input("Press enter/return to continue....")
print(f"\n******Final score******\nPlayer 1: {score[0]} \nComputer: {score[1]}")

match(score):
    # This little number is called pattern matching with an if-guard. This is something newer (2021) in python im learning.
    case [x,y] if (x > y):
        print("Player 1 wins!")
    case [x,y] if (x == y):
        print("Tie!")
    case [x,y] if (x < y):
        print("Computer wins!")

