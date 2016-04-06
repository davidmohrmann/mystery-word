# this program will ask the user to guess letters in order to spell out a random word that was selected from a predetermined directory
# if the user guesses the word in 8 tries, he wins; if not, he loses
# the user can select the difficulty of the challenge, Easy, Medium, or Hard.

#import the random library
import random
#import regex so can scrub any punctuation that might come up
import re


# an empty list that will collect all the words from the document, when it goes word by word
Master_random_word_list = []
# an empty list that is collecting the total number of guesses made by the player
# the total guesses CAN NOT be more than 8.
total_guess = []

easy_list = []
medium_list = []
hard_list = []


# be able to read from the word directory that Bryce instructed us to use
with open('/usr/share/dict/words', 'r') as file:
    # split at each '', breaking the list up into individual words.
    for word in file:
            # by using this scrub method, we were able to take out the \n at the end of the words and make
            # all lowercased
            word = re.sub('[^A-Za-z]', '', word).lower()
            # for word in word:
            Master_random_word_list.append(word)

###
### Probably could have put all of these functions into one with an If: Else statement! ####
###

def easy_word():
    for word in Master_random_word_list:
        if len(word) <= 6:
            easy_list.append(word)


def medium_word():
    for word in Master_random_word_list:
        if len(word) >= 7:
            medium_list.append(word)


def hard_word():
    for word in Master_random_word_list:
        if len(word) >= 9:
            hard_list.append(word)
            


# now that we have a random list, computer needs to randomly select a number from the list
# could have selected a random item from the range of the list being range(0: len(random_word_list-1))
    # the above would have determined the length of the list and then gone to the end of the range, and inclued the last numbers
    # since not completely sure, we will use the .choice method we found online.

def Welcome_to_the_Thunder_Dome():
    #Print an intro to our new game
    print("I think we should play a game!")
    print("Let's see if you can guess the word that I have randomly thought of in 8 tries!")
    #print an extra line, to make it look pretty
    print()


def chooseDifficulty():
    # New variable called difficulty
    # this function will only allow the player to enter: e, m, or h. They will be automatically lowercased.
    # if the input is anything but, e, m, or h, spit out.
    while True:
        difficulty = input("What level woud you like to play? E for Easy, M for Medium, or H for Hard? ").lower()

        if difficulty == 'e':
            print('This game will be easy.')
            break
        elif difficulty == 'm':
            print('This game will be medium.')
            break
        elif difficulty == 'h':
            print('This game will be hard.')
            break
        else:
            print("Sorry, that isn't an option.")
            # put a continue in there so it will keep asking you to input a difficutly level!
            continue
        print()


def random_word():
# Return a random word from the sublists of Master_random_word_list.
    word = Master_random_word_list
    random_word = random.choice(word)
    '''this does not print out the correct number length of the random word
    print (("The length of your word is " + str(len('random.choice(word)')) + ' letters!'))'''
    print (random.choice(word))
    return (random.choice(word)) # needs to be changed to return so player can't see it


def player_guess():
# We need to store the player's letter guess in the total_guess list.
# we run a while loop which states that while the total_guess is less than 9
# allow guesses to still be made
# since we are using a list to store this info, we need to know the lenght
# of said list to determine how many guesses are left.
# total_guess is a Global variable
    while len(total_guess) <9:
        # now, we need some input from the player about his guesses. This Would
        # be what letter he wants to guess.
        letter = input("Why don't you guess a letter to see if its in the word? ")
        # the player needs to enter EXACTLY one alpha character at a time.
        # if the length of the input is not one, inform the player.
        # if letter in random_word:
        #     print("That letter is in the word!")
        if len(letter) != 1:
            print("Please enter only one letter at a time.")
            continue
        # else if the player's input is not a letter in the alphabet, inform the player (no other characters)
        elif letter not in 'abcdefghijklmnopqrstuvwxyz':
            print("We are guessing a word. That character is not alpha!")
            continue

############ I need to have the player's guess go against the word count!##############
        # else if, the guess has already been guessed, do not deduct from 9 tries
        # make a local variable so can store the redundant guesses
        elif letter in total_guess:
            guess_already_in_total_guess = total_guess
            print("You have already guessed that letter!")
            continue

        else:
            # if letter in random_word:
            #     print("You got a letter in the word!")
            # else:
            #     print('That letter is not in the word!')
            total_guess.append(letter)
            print ('Your guesses: ' + str(total_guess))





Welcome_to_the_Thunder_Dome()
easy_word ()
medium_word ()
hard_word ()
chooseDifficulty()
random_word()
player_guess()
