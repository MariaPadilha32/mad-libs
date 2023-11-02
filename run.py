import importlib
from food import foodStories
from movies import moviesStories
from nurseryrhymes import nurseryStories
from random import randomStories
from music import musicStories


def welcome_message():
    """
    Basic instructions for the user to follow while playing the game.
    """
    print("Welcome to Mad Libs!")
    print("The objective of the game is to create the funniest story possible.")
    print("You will be prompted to input various words (nouns, adjectives, verbs, adverbs, etc.),")
    print("and these words will be used to fill in the blanks in a story.")
    print("Enjoy the result of your Mad Libs!\n")

def mad_libs_game():
    """
    Main function that runs the game
    """
    while True:
        welcome_message()
        print("First, pick a subject:")
        print("1 - Food")
        print("2 - Music")
        print("3 - Movies")
        print("4 - Nursery Rhymes")
        print("5 - Random")

        while True:
            try:
                subject_choice = int(input("Enter the subject number (1 to 5): "))
                if 1 <= subject_choice <= 5:
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")

        subject_module = None
        if subject_choice == 1:
            import food as subject_module
        elif subject_choice == 2:
            import music as subject_module
        elif subject_choice == 3:
            import movies as subject_module
        elif subject_choice == 4:
            import nurseryrhymes as subject_module
        elif subject_choice == 5:
            import random as subject_module

        # Run the selected subject's mad libs
        subject_module.run_mad_libs()
 
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing!")
            break


if __name__ == "__main__":
    mad_libs_game()


