import random

plays = ["Rock", "Paper", "Scissors"]
selection = int(input("How many rounds do you want to play? Enter a number: "))
player_1_plays = [random.randint(0, 2) for _ in range(selection)]
player_2_plays = [random.randint(0, 2) for _ in range(selection)]
score = [0, 0]


for i in range(selection):
    print(f"Round {i+1}:")
    print("Player 1:", plays[player_1_plays[i]])
    print("Player 2:", plays[player_2_plays[i]])
    if (player_1_plays[i] == 0):
        if(player_2_plays[i] == 1):
            print("Player 1 losses\nPlayer 2 wins")
        elif(player_2_plays[i] == 0):
            print("Tie")
        else:
            print("Player 1 wins\nPlayer 2 losses")
    if (player_1_plays[i] == 1):
        if(player_2_plays[i] == 2):
            print("Player 1 losses\nPlayer 2 wins")
        elif(player_2_plays[i] == 1):
            print("Tie")
        else:
            print("Player 1 wins\nPlayer 2 losses")
    if (player_1_plays[i] == 2):
        if(player_2_plays[i] == 0):
            print("Player 1 losses\nPlayer 2 wins")
        elif(player_2_plays[i] == 2):
            print("Tie")
        else:
            print("Player 1 wins\nPlayer 2 losses")
            

    input("Press enter/return to continue....")

