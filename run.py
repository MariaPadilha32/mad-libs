"""
Importing necessary modules & files
"""
import importlib
import random
from time import sleep
from food import foodStories
from movies import moviesStories
from nurseryrhymes import nurseryStories
from randStories import randStories
from music import musicStories
from utils import get_non_empty_input

def welcome_message():
    """
    This function is to welcome the user
    and give basic instructions on how the game works
    """
    print("Welcome to Mad Libs!\n")
    print("The objective of the game is to create the funniest story possible.")
    print("You will be prompted to input various words (nouns, adjectives, verbs, adverbs, etc.),")
    print("and these words will be used to fill in the blanks in a story.")
    print("Enjoy the result of your Mad Libs!\n")
    

def mad_libs_game():
    """
    Main function that runs the game
    """
    while True:
        print("First, pick a subject:\n")
        print("1 - Food")
        print("2 - Music")
        print("3 - Movies")
        print("4 - Nursery Rhymes")
        print("5 - Random\n")
        

        while True:
            try:
                sleep(2)
                subject_choice = int(input("Enter the subject number (1 to 5): \n"))
                if 1 <= subject_choice <= 5:
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")
                
         
        if subject_choice == 1:
            foodStories()
        elif subject_choice == 2:
            musicStories()
        elif subject_choice == 3:
            moviesStories()
        elif subject_choice == 4:
            nurseryStories()
        elif subject_choice == 5:
            randStories()

        sleep(3)
        play_again = get_non_empty_input("\nPlay again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThank ou for playing! \nThis game is part of a Code Institute project.\nIf you'd like to explore more of my work,\nplease visit my GitHub profile: https://github.com/MariaPadilha32?tab=repositories")
            break
        
if __name__ == "__main__":
    welcome_message()
    mad_libs_game()