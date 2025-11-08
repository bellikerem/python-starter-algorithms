"""
    
    Developer: Kerem Can Belli
    Project: Python Starter Algorithms and CLI Applications
    Subproject: Hangman Game
    Description: Updated English version with structured comments
    Last Review: November 2025

"""

##########################################################################

"""

    * Random method is added.
    * Guess and word_pool variables are identified.

"""

import random

guess = 5

word_pool = {
    "Name" : ["Kerem", "Alper", "Engin", "Hatun", "Emirhan", "Sefa", "Utku", "Berat", "Burak", "Bulent", "Mehmet", "Zeynep", "Nehir",
    "Ayse", "Fatma", "Zuleyha", "Zahide", "Ali", "Ahmet", "Omer", "Kasim", "Sabri"],
    
    "City" : ["İstanbul", "Ankara", "İzmir", "Antalya", "Trabzon", "Eskisehir", "Kocaeli", "Sivas", "Malatya", "Konya"],
    "Country" : ["Turkiye", "Almanya", "Fransa", "İngiltere", "İspanya", "Hollanda", "Amerika", "Japonya", "Rusya", "İtalya","Meksika", 
              "Brezilya", "Arjantin", "Portekiz"],
    "Animal" : ["Horse", "Donkey", "Lion", "Eagle", "Canary", "Fish", "Bear", "Panda", "Koala", "Snake", "Crocodile", "Chicken", "Cow"],
    "Herb"  : ["Orchid", "Rose", "Poppy", "Violet", "Daisy", "Tomato", "Cucumber", "Onion", "Herb"],
    "Furniture"   : ["Computer", "Telephone", "Glasses", "Armchair", "Table", "Chair", "Lamp", "Notebook", "Pencil"]
}

##########################################################################

"""

    Hangman game main menu:

    * Users decide the game's category.
    * Input is validated using try-except blocks to handle non-integer input.

"""

print("\n--- HANGMAN GAME ---")
while True:
    try:
        choice_input = input("Please choose your category: \n" \
        "Press 1 for name \n" \
        "Press 2 for city \n" \
        "Press 3 for country \n" \
        "Press 4 for animal \n" \
        "Press 5 for herb \n" \
        "Press 6 for furniture: ")
        choice = int(choice_input)
        if choice not in [1,2,3,4,5,6]:
            print("Enter an integer between 1 - 6.")
            continue
        break
    except ValueError:
        print("Please input an integer.")

##########################################################################

def random_word_choice(category):

    """
    
    * The game's word is selected randomly depends on users preference.
    * All letters in the word is converted to lower case.
    * The word is hidden by using "_" and changed to "secret_word".

    Args:
        category (str): The category that users decide for game's word

    """

    random_choice = random.choice(word_pool[category])
    proper_word = random_choice.lower()
    secret_word = ["_"]*len(proper_word)

    return proper_word, secret_word

##########################################################################

def game_loop(proper_word, secret_word, guess):

    """
    
    * The goal and guesses are showed.
    * Congratulations and loss messages are displayed.
    * Letter that users guess is checked whether it is in word or not.
    * guess variable is reduced if users make wrong letter guess.

    """

    print("You have 5 guesses. The goal is to find the secret word before your guesses run out.")
    while True:
        print(secret_word)
        if "_" not in secret_word:
            print(f"CONGRATULATIONS! YOU FIND THE SECRET WORD: {proper_word}")
            break
        if guess == 0:
            print(f"UNFORTUNATELY YOU LOST. THE SECRET WORD IS: {proper_word}")
            break
        letter_guess = input("Enter one of the lower case letters: ")
        if letter_guess not in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u",
                               "v","y","z","x","q","w"]:
            print("Please input one of the lower case letters.")
            continue
        if letter_guess in proper_word:
            print("CORRECT GUESS")
            letter_check = False
            for i, letter in enumerate(proper_word):
                if letter == letter_guess:
                    secret_word[i] = letter
                    letter_check = True
        else:
            print("WRONG GUESS")
            guess -= 1
            print(f"GUESS: {guess}")
    return guess

                
##########################################################################

"""

    * The category value is assigned by the system based on the user's request.
    * game_loop function is executed.

"""


if choice == 1:
    word, current_secret = random_word_choice("Name")
    game_loop(word, current_secret, guess)
elif choice == 2:
    word, current_secret = random_word_choice("City")
    game_loop(word, current_secret, guess)
elif choice == 3:
    word, current_secret = random_word_choice("Country")
    game_loop(word, current_secret, guess)
elif choice == 4:
    word, current_secret = random_word_choice("Animal")
    game_loop(word, current_secret, guess)
elif choice == 5:
    word, current_secret = random_word_choice("Herb")
    game_loop(word, current_secret, guess)
else:
    word, current_secret = random_word_choice("Furniture")
    game_loop(word, current_secret, guess)