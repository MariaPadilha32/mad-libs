import gspread
import json
import os
import random

json_files = [
    'templates/animal_libs.json',
    'templates/food_libs.json',
    'templates/holiday_libs.json',
    'templates/movies_libs.json',
    'templates/nursery_rhyme_libs.json',  
    'templates/sports_libs.json'
]

def load_template(subject_number):
    with open(json_files[subject_number - 1], 'r') as file:
        template = json.load(file)
    return template


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
    while True:
        welcome_message()

        print("First, pick a subject:")
        for i, subject in enumerate(json_files, start=1):
            print(f"{i} - {subject.split('/')[1].split('_libs')[0].capitalize()}")

        while True:
            try:
                data_str = int(input("Enter the subject number (1 to 6): \n"))
                if 1 <= data_str <= 6:
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and 6.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 6.")

        subject_number = data_str
        template = load_template(subject_number)

        user_inputs = {}
        for key, value in template.items():
            if key != "story":
                user_inputs[key] = input(f"Enter a {value}: \n")

        final_story = template["story"].format(**user_inputs)
        print("Here's your Mad Libs story:")
        print(final_story)

        play_again = input("Play again? (yes/no): \n").lower()
        if play_again != "yes":
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    mad_libs_game()
