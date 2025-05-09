import random

#The playable options
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

#FUNCTIONS
#This function matches user input to the appropriate array index so that they can type their input in either case(lower/upper) or simply enter a number
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
#This function prints the winner of the game.
def scoreBoard(score):
    match(score):
        # This little number is called pattern matching with an if-guard. This is something newer (2021) in python im learning.
        case [x,y] if (x > y):
            return "Player 1 wins!"
        case [x,y] if (x == y):
            return "Tie!"
        case [x,y] if (x < y):
            return "Computer wins!"
#This function checks for winner instance of a match
def checkBattleResult():
    if (player_1_plays[i] == 0):
        if(computer_plays[i] == 1):
            score[1] += 1
            return "Computer wins, +1 Point"
        elif(computer_plays[i] == 0):
            return "Tie - No Points"
        else:
            score[0] += 1
            return "Player 1 win +1 Point"
            
    if (player_1_plays[i] == 1):
        if(computer_plays[i] == 2):
            score[1] += 1
            return "Computer wins, +1 Point"
        elif(computer_plays[i] == 1):
            return "Tie - No Points"
        else:
            score[0] += 1
            return "Player 1 win +1 Point"
            
    if (player_1_plays[i] == 2):
        if(computer_plays[i] == 0):
            score[1] += 1
            return "Computer wins, +1 Point"
        elif(computer_plays[i] == 2):
            return "Tie - No Points"
        else:
            score[0] += 1
            return "Player 1 win +1 Point"
    else:
        return "Problem, error occured...."  

#Main gameplay loop.
for i in range(selection):
    print(f"******* Round {i+1} *******")

    #Input validation loop, if the user gives invalid input then we continue requesting. If correct, assign it to 'answer' and break from validation loop.  
    while (True):
        choose = str(input("What will you play? 1. Rock, 2. Paper, or 3. Scissors? "))
        answer = userGameChoice(choose, i)
        print(answer+"\n")
        if(answer.startswith("Invalid")):
            continue
        else:
            break
    
    #These two prints print the current play along with the corresponding ascii art.
    print(f"Player 1: {plays[player_1_plays[i]]} \n{ascii_art[(plays[player_1_plays[i]].lower())]}")
    print(f"Computer: {plays[computer_plays[i]]} \n{ascii_art[(plays[computer_plays[i]].lower())]}")
    
    #Check win/lose/tie
    print(checkBattleResult())

    #With selection-2 we remove the input on the final round of game play.      
    if(i <= selection-2):
        input("Press enter/return to continue....")
        
#Final score print, calls the scoreBoard function to calculate a result and print.
print(f"\n******Final score******\nPlayer 1: {score[0]} \nComputer: {score[1]}")
print(scoreBoard(score))
