"""
This is a beginner-friendly text-based decision-making game that demonstrates core Python logic and input handling.
It was designed to reinforce the use of nested conditionals and user input via the command line.

    Concepts used here include:
        1. If/elif/else conditionals (with multiple layers of nesting)
        2. String input manipulation
        3. Boolean flags for game control

    Future additions to consider:
        1. Implementing a thirst level system, and dialogue options to increase and decrease thirst.
        2. Adding randomized events for more dynamic gameplay.
        3. If 1. is implemented further guide the game towards finding large source of fresh water.
"""
print("""
  ....                .....:-==+====*##*+. ....                 ....       .....    .....            
...                 ....=%%%%%###***###*=...                 ....                .....     ...      
.                 ...  .+%%%%%%%%#**####*=                  ...                 ....      :%#=-:... 
                ....   .*%%%%%%%%%###%%%#*-               ...                 ....  ..:---=*=:.:-==.
  ...         ....    .:#%%%%%%%%%#%%%%###*-..  .:-===:.....                ....:-------=-+.=%%#*--+
 .....      ....      .=%%%%%%%%%%%%%######+:=*#%%%%%%%=..     .-=:.    ..:---==-=+*####%%+=%%%%**:*
 .......   .:===-..  .:#%%%%%%%%%%%#####%%##%%#%%%%%%%%=.       -+*---=-===+*##%%%%%#****+#=+%%#*+-+
   ........+%%%%%%#+-.-%%%%%%%%%%%%%%%######%%%##%%%%%*:       .-**+####%%%%########%%%%%%##*+==+*+:
     ......#%%%%%%%%%%#%%%%%%%%%############%%%%%#%#%*:.     ..==-::#####%%%%%%%%%%%%%%%%%%#%%%%+...
     ......:+%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*-..      .+===*##+%%%%##%%#############%*==+-.  
   ....  .....:--=+*%%%%%%%%%%%%%%%%%%%%%%%%%%%%#=:.......   :%#*=+*+#%%%%+=%%#%%%%%%%##**+##*++-...
 ....      .....    ..-#%%%%%%%%%%%%%%%%%%%%#=:..   ......   :%%%+-+*%%%%%+=%%*%%%:.....   .........
...         ...      ..-%%%%%%%%%%%%%%%%%%%%=.        ...    .*%%#*#%%%%%#**%%#%%*....          ... 
.                  ... ..+%%%%%%%%%%%%%#*=*+.               ...+%%%#*#%%##%%%#%%%...                
                 ...    .=%%%%%%#-:--=*#+==+              ...  .-#%%%%%%%%%%%%%%%:                  
               ....      :*%%%%%*-----:-*==+            ..-*===+#%#***%%%%%%%%%%%.                ..
             ....     ....*%%%%%#=+:-+===++*.         ....#=:::-=#%%%+%%%%%#+**:..              ....
           ....       ....+%%%%%%#+::--=+-=*+-.     .... :#--:-=-*#%%%%%%*-:::==              ....  
          ...          ...-*=#%%%%%*=--+##*=+%#+=-::..   -%*:::++#%%*=-*%+:---+-            ....    
        ...              .+#=-+*%%%%%%%#*++#%%%%%%%%%%%#*#%#+==+#%#+===+.==*#**-.          ...      
      ....            ..=**#*-=*#%#****+*%%%%%%%%%%%%%%%*+#%%%%%%%*=--=*-+%#=-:--        ...        
    ....            .=#%#%%%#=+#%%%%#*+#%%%%%%%%%%%%%%#+==+%====-=+###%#=+=::::=-      ...          
  ....          .:*#%%%%%%*#%#%#****#%%%%%%%%%%%%%%%%%+++*%#*-----==+%%%#+-:::=*.    ....           
 ...           .-#**%%%%%*+*%++++++++#%%%%%%%%%%%%%%%*++*#*#%#+==-=**+**+=--:::#.......             
..             .+*+#%%%%%*+**++++++++#%%%%%%%%%%%%%%%+++#**%%#=======--:::::::*=.-...               
               .+*+%%%%%#++*+=++++++*%%%%%%%%%%%%%%%#++***#%%#=----=--::::::::#.:=.                 
              .:+++%%%%%#*+*+*++++++#%%%%%%%%%%%%%%%*+++##%%%%%#+==+#+**=-:::-#:.*.               ..
 ...         ..:++*%%%%%%*+*++++++++#%%%%%*%%%%%%%%%++++##%%%%%=======--::-=**:.==:......       ....
 .....     ....:++*%%%%%%*+*++++++++#%%%%+-*##%%%%%%*+++###%%%%%#*++=+#+#%*-..:*--+.......    ..... 
 ........ .... :++*%%%%%%*+*+++++++*%%#=-----+%%%%%%**++*###%%%%%%%%%%%%%*...:.-#-.  ...... .....   
   .........   :++#%%%%%%*+++++++++*%%%%+--=*%%%%#%%*##+++#%#******#%%#%%-. .::...     ........     
     ......    :++#%%%%%%*+++++++++*%%%%+*%+*%%%%%%#*#%#**++******##**%%:.               .......    
    .........  .++#%%%%%%*+++++++++*%%%%%%%%%%%%%%%#*##%%*********##*#%:. ...          ..........   
  ....    ......+**%%%%%#++*+++++++*%%%%%%%%%%%%%%%%**##%%%#********#%=.  ...        ....    ...... 
 ...       .....+**%%%%%#++*+++++++*%%%%%%%%%%%%%%%%%**%%%%%%%%%%%%%*.    .:.      ....        .... 
..             .=**%%%%%#++#+++++++*%%%%%%%%%%%%%%%%%#*#%%%= ....::.       -:.   ....               
               .=##%%%%%#++#+++++++*%%%%%%%%%%%%%%%%%%##%%%:..             -:.  ...                 
              .:*%#%%%%%*++#+*+++++*%%%%%%%%%%%%%%%%%%%%%%%.              .--....                  .
             ..+#*#%%%%%*++#+++++++*%%%%%%%%%%%%#%%%%%%%%%%.   .....      .--...                ....
           ...-***%%%%%#++**+++++++*%%%%%%%%%%%#%%%%%%%%%%%.   ......    ..-:...              ....  
          ....+***%%%%%#==**+++++++*%%%%%%%%%%#%%%%%%%%%%%%:    ...... ...-=..:.            ....    
        .....-*+*#%%%%%#++*++++++++*#%%%%%%%%%%%%%%%%%%%%%%+.     ........==.-:.           ...      
      .... .:*++*%%%%%%*+*#+===++++*#%%%%%%%%%%%%%%%%%%%%%%%.       .....:=:.-.          ...        
    ....  .:*+++*%%%%%%*+**++===+++*#%%%%%#%%%%%%%%%%%%%%%%%.     .......-=.=-.        ...          
  ....   .:*++++%%%%%%%*+#*++++==+**#%%%%#%%#%%%%%%%%%%%%%%%:   .....  .:+:-=.       ....           
 ...    .=*++++*%%%%%%%*+#*++++++++*%%%%%%#%%%%%%%%%%%%%%%%%- ....     .+-:=:..    ....             
..     .:*++++*#%%%%%%%#*#*++*******%%%%%%%%%%%%%%%%%%%%%%%%:...      .==:+-.    ....               
       .+#*++**%%%%%%%%#*##********#%%%%%%%%%%%%%%%%%%%%%%%%..       .-+.+-.    ...                 
     ..=*++***#%%%%%%%%#*###*******#%%%%%%%%%%%%%%%%%%%%%%%%.       .-+.+-.   ...                  .
 .....=*******#%%%%%%%%%%####******#%%%%%%%%%%%%%%%%%%%%%%%+.      .-=.*:   ....    ....         ...
 ....-+++*###%%*-..*%%%%%##%%%%%%%%%%%%%%%%%#%%%%%%%%%%*-.        .=--*.  ....      .....      .... 
 ..:==::::-%%=.   .+###%%###+=+%%%%%####%%%%###%%%%%%%#+.        .=-+-. ....        .......  ....   
 .:+-:::::-*.     .#*****#*+**%%##%%%%%%%%%%##***####*##-.     .:--=:. ...            .........     
.-*:::==::+=      :#*******##*#%*******#%%%%#**********#=.    .:---. ...                .......     
:*-:-**=:+=.     .+#*******##*#%********#%%%%%##*******#=.   .:::. ...                  .. .....    
+=-=*++=+-.....  .*#********#*#%**********#%%%%%%##****#*:. .... ....                 .... ........ 
#==*====+....... .#*********#**#************##%%%%%%##*##*##*+-....                 ....     ...... 
*++%+-+*-. ....  :#*********#**#***************#####%%*##%%%%%%#:                 ....         ...  
#*=##-.          -#****###*****##******####******###%%#**#%%%%%*.                ...                
:##+#=.         .+#*****####**###**######*******####%%%##*****%*.              ...                 .
.:=++:        ...*#*******############*******#######%%##%%%###%+.            ...                 ...
            .....*#*****############################%%%%%%##%%%=....       ....                .....
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                _     _   _                     __                    
                ' )   /   //                    /  )         /         
                / / /_  // _. __ ______  _    /   __ , , , /____ __  ,
                (_(_/</_</_(__(_)/ / / <_</_  (__/(_)(_(_/_/_)(_)/ (_/_
                                                                    /  
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
""")
choice = input("You wake up in the desert. Throat dry. Sun blazing. You find a small satchel with a few items and a note that reads: 'Only one path leads home. Choose wisely.'\n\nMake a selection:\nA. Drink the urine you have been saving in a bottle.\nB. Sit and dig in the dirt.\nC. Eat a cactus.\nD. Walk toward a silhouette in the distance.\n> ").strip().upper()

incorrectInput = False
gameOver = False
uniqueEnd = 0

endLoseMessage = "Loser! You have failed. Try again next time."
endWinMessage = "Winner, wow you really got past my BS. Good job, if you did it on your first attempt, that is."

gameStatus = endLoseMessage

while not gameOver:
    if choice == "A":
        print("\nIt's salty, unsettling... oh no, it's definitely urine. You vomit, dizzy, vision fades.")
        uniqueEnd = 1
        gameOver = True

    elif choice == "B":
        print("\nYou sit and dig... inch by inch. Sun scorches your back.")
        choice = input("\nDo you keep digging?\nA. Yes\nB. No, this is madness.\n> ").strip().upper()

        if choice == "A":
            print("\nFingers bloody, sanity fading. Hours pass. You collapse in the hole you made.")
            uniqueEnd = 2
            gameOver = True
        elif choice == "B":
            print("\nYou sit back and sigh. What now?")
            choice = input("\nYou hear a buzzing sound nearby. Investigate?\nA. Yes\nB. No, sounds dangerous.\n> ").strip().upper()

            if choice == "A":
                print("\nYou follow the sound to find an old radio half-buried in the sand. It crackles to life.")
                choice = input("\nUse the radio?\nA. Try to call for help\nB. Smash it in paranoia\n> ").strip().upper()

                if choice == "A":
                    print("\nYou call for help. A voice responds: 'Help only comes to those who help themselves.' The radio sparks and dies.")
                    choice = input("\nFrustrated, you look up and see a hatch nearby. Try to open it?\nA. Yes\nB. No\n> ").strip().upper()

                    if choice == "A":
                        print("\nIt creaks open. A ladder descends into darkness. You climb down.")
                        print("\nYou awaken... in your bed. Was it all a dream? You win.")
                        gameStatus = endWinMessage
                        uniqueEnd = 99
                        gameOver = True
                    else:
                        print("\nYou walk away, the hatch disappears behind you. You wander endlessly.")
                        uniqueEnd = 3
                        gameOver = True
                else:
                    print("\nYou smash your only lifeline. The buzzing is replaced by silence. You die slowly.")
                    uniqueEnd = 4
                    gameOver = True
            else:
                print("\nYou ignore the buzzing. Days pass. No rescue. No salvation.")
                uniqueEnd = 5
                gameOver = True

    elif choice == "C":
        print("\nYou cut open a cactus and drink its contents. It’s bitter... too bitter.")
        print("\nYou hallucinate wildly. You forget where, who, even what you are.")
        print("As reality bends, a hole opens beneath you. You fall into darkness.")
        uniqueEnd = 6
        gameOver = True

    elif choice == "D":
        print("\nYou approach a figure. He looks rough. You both eye each other, unsure of intent.")
        choice = input("\nChoose your action:\nA. Attack him.\nB. Talk.\nC. Slowly back away.\n> ").strip().upper()

        if choice == "A":
            print("\nYou attack wildly. He was stronger. You lose.")
            uniqueEnd = 7
            gameOver = True
        elif choice == "B":
            print("\nHe smiles. ‘Nice to see someone civilized,’ he says.\nHe gives you a map and disappears.")
            choice = input("\nFollow the map?\nA. Yes\nB. No, it could be a trap.\n> ").strip().upper()

            if choice == "A":
                print("\nYou follow it... into quicksand. Oops.")
                uniqueEnd = 8
                gameOver = True
            else:
                print("\nYou toss the map. You end up walking in circles. A vulture circles above.")
                uniqueEnd = 9
                gameOver = True
        else:
            print("\nYou back away awkwardly. He watches, disappointed.")
            print("Eventually, dehydration gets you.")
            uniqueEnd = 10
            gameOver = True
    else:
        print("\nThat wasn't a valid option. Type a letter you fool.")
        choice = input("Try again. A, B, C, or D?\n> ").strip().upper()

print("\n" + gameStatus)

match uniqueEnd:
    case 1:
        print("Wow that was quick. Didn't expect you to go with that right off the bat. Drinking pee? Gross.")
    case 2:
        print("You really dug yourself into a hole, huh. *drum roll*")
    case 3:
        print("You ignored the way out. So close, yet so far.")
    case 4:
        print("Trust issues, huh? Sometimes the answer is a call away.")
    case 5:
        print("Paranoia doesn't always keep you alive.")
    case 6:
        print("Cactus trip, anyone? You turned into a philosopher of the void.")
    case 7:
        print("Violence isn't always the answer... especially when you're weak.")
    case 8:
        print("Map led you right into a trap. Classic.")
    case 9:
        print("You tried to be clever and ended up lost. Irony.")
    case 10:
        print("Should’ve committed to *something*, my dude.")
    case 99:
        print("You actually won! The obscure path was yours to claim. Respect.")
    case _:
        print("What a basic ending. Kinda lame if you ask me.")
