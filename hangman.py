# Chapter 10 challenges
""" create a text-based Hangman game """

def hangman(word):
    
    # track number of wrong guesses
    wrong = 0
    
    # keep a list of stages of Hangman
    stages = ["",
              "________        ",
              "|               ",
              "|       |       ",
              "|       0       ",
              "|      /|\      ",
              "|      / \      ",
              "|               "
              ]
    
    # create a list of letters from the guess word
    rletters = list(word)

    # generate a board where an underscore represents each letter in the guess word
    board = ["_"] * len(word)

    win = False
    print("Welcome to Hangman")

    # while the player still has guesses remaining
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)

        # if player guesses correct letter
        if char in rletters:

            # get the index of that letter in the list of letters
            cind = rletters.index(char)

            # update board list to replace underscore with correct letter
            board[cind] = char

            # replace letter with $ so it's not checked again
            rletters[cind] = '$'

        else:
            wrong += 1

        # print the board with a space between each letter
        print("\n")
        print((" ".join(board)))

        # get the index of the stages list for the amount of incorrect guesses
        e = wrong + 1

        # print the Hangman with a new line between each string by slicing the stages list
        print("\n".join(stages[0:e]))

        # if no un-guessed letters remain
        if "_" not in board:
            print("You win! \n")
            # display correctly guessed word back to player
            print(" ".join(board))
            win = True
            break
        
    if not win:
        # print complete Hangman
        print("\n".join(stages[0:wrong]))
        # display lose message and the word to the player
        print("You lose! it was {}.".format(word))

import random

words = [
    "dog",
    "cat",
    "ball",
    "rope",
    "car",
    "book",
    "boat",
    "drink",
    "food",
    "pillow",
    "blanket",
    "radio",
    "game",
    "computer",
    "remote",
    "soft",
    "hard",
    "sand",
    "paper",
    "goat",
    "bear",
    "lion",
    "vinny",
    "aladdin"
    ]

# make the game select a random word from the words list
wrd = words[random.randint(0, len(words) - 1)]

# run the Hangman game
hangman(wrd)
