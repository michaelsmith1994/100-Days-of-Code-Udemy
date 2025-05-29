from random_words import RandomWords
rw = RandomWords()
word = rw.random_word()

blank_key = len(word)*' _ '
word_arr = [characters for characters in word]
guesses = []
fill_in_blank = blank_key.split()

#Hang man ascii art thanks go to chrishorton: "https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c"
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

attempts = 6

def print_hanging():
    print(HANGMANPICS[6-attempts])

def print_fill_in_blank():
    printable = ""
    if(attempts != 0):
        for characters in fill_in_blank:
            printable += str(characters + ' ')
        print(printable)

def check_for_letter(c):
    if c in word_arr:
        print("You found a letter!")
        return(True)
    else:
        print("Missed letter!")
        print("Attempts remaining: " + str(attempts))
        
        print_hanging()
        if(attempts == 0):
            print("***************************")
            print("No attempts remaining... YOU LOSE ...\nThe word was "+word)
            print("***************************")
        return(False)


def add_letter_to_blank(c):
        for i, char in enumerate(word_arr):
            if char == c:
                fill_in_blank[i] = c

#Game start
while(attempts >= 0):
    print_fill_in_blank()
    states = False
    guess = input("Guess a letter: ").lower()

    if guess in guesses:
        print("You already guessed that, try again.")
        continue
    else:
        guesses.append(guess)
        print("So far you have guessed: "+str(guesses))

    states = check_for_letter(guess)
    
    if states == True:
        add_letter_to_blank(guess)

        if "_" not in fill_in_blank:
            print("You win!")
            break
        else:
            continue

    else:
        ##Here we should add a dict of ascii art and reference 7 ascii figures indexed 0-6
        ##Math ~ ~ dictionary[6-attempts]
    
        attempts -= 1
        

