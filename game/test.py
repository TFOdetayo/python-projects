# I want to give the player 9 lives
# i want them to guess

#start game
#here we play
#display the lives
#check answer

import random

lives = 9
words = ['pizza', 'fairy', 'teeth', 'shirt', 'otter', 'plane']
hidden_word = random.choice(words)
hidden_word_length = len(hidden_word)
clue = hidden_word_length * '_'
letter = input("Pick a letter: ")

def start():
    print("Welcome to the Guess Word Game!")
    print(clue)
    while game():
        pass

def game():
    choose_word()
    check_lives()
    play_again()

def choose_word():
    while letter != hidden_word:
        index = 0
        while index < hidden_word:
            if letter == hidden_word[index]:
                clue[index] = letter
            index = index + 1

def check_lives():
    if letter not in hidden_word:
        print('Incorrect. You lose a life')
        lives = lives - 1
    check_answer()

def check_answer():
    if hidden_word == clue:
        print('You won! The secret word was ' + hidden_word)
    else:
        print('You lost! The secret word was ' + hidden_word)

def play_again():
    answer = input("Would you like to play again? y/n: ")
    if answer in ("y", "Y", "yes", "Yes", "of course", "sure"):
        return answer
    else:
        print ("Thank you very much for playing our game. See you next time!")

start()