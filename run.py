"""
Importing necessary modules & files
"""
import importlib
import random
import os
from time import sleep
from food import foodStories
from movies import moviesStories
from nurseryrhymes import nurseryStories
from randStories import randStories
from music import musicStories
from utils import get_non_empty_input
from utils import get_numeric_input


def welcome_message():
    """
    This function is to welcome the user
    and give basic instructions on how the game works
    """
    print("Welcome to Mad Libs!\n")
    print("The objective of the game is to create the funniest story possible")
    print("You will be prompted to input various words")
    print("such as nouns, adjectives, verbs, adverbs, etc.,")
    print("and these words will be used to fill in the blanks in a story.")
    print("Enjoy the result of your Mad Libs!\n")


def mad_libs_game():
    """
    Main function that runs the game - allows the user to select a subject
    input they choice, play different stories, play again or exit
    """
    while True:
        print("First, pick a subject:\n")
        print("1 - Nursery Rhymes")
        print("2 - Music")
        print("3 - Movies")
        print("4 - Food")
        print("5 - Random\n")

        while True:
            try:
                sleep(2)
                subject_choice = int(input("Pick a subject number (1 - 5):\n"))
                if 1 <= subject_choice <= 5:
                    break
                else:
                    print("Invalid input. Please pick a number between 1 - 5.")
            except ValueError:
                print("Invalid input. Please pick a number between 1 - 5.")

        if subject_choice == 1:
            nurseryStories()
        elif subject_choice == 2:
            musicStories()
        elif subject_choice == 3:
            moviesStories()
        elif subject_choice == 4:
            foodStories()
        elif subject_choice == 5:
            randStories()

        sleep(3)
        play_again = get_non_empty_input("\nPlay again? (y/n): ").lower()
        if play_again != "y":
            print("\nThank you for playing!"
                  " \nThis game is part of a Code Institute project.\n"
                  "If you'd like to explore more of my work,"
                  "\nplease visit my GitHub profile:"
                  "https://github.com/MariaPadilha32?tab=repositories")
            break
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    welcome_message()
    mad_libs_game()
