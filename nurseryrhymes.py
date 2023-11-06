"""
inport the necessary functions to make sure users
will not input incorrect information only alphabetic characters
"""
from utils import get_non_empty_input

def nurseryStories():
    girls_name_nr = get_non_empty_input("Enter a Girl's Name: ")
    animal_nr = get_non_empty_input("Enter an Animal: ")
    color_nr = get_non_empty_input("Enter a Color: ")
    place_nr = get_non_empty_input("Enter a Place: ")
    verb_nr = get_non_empty_input("Enter a Verb: ")

    nursery_story = (
       "\n" + girls_name_nr + " had a little " + animal_nr + " little " + animal_nr + " little " + animal_nr + ". \n" +
        girls_name_nr + " had a little " + animal_nr + ", its fleece was " + color_nr + " as snow.\nIt followed her to " + place_nr + " one day, " + place_nr + " one day, " + place_nr + " one day,\n" +
        "it made the children " + verb_nr + " and play to see " + animal_nr + " at " + place_nr + ".\n"
    )
    print(nursery_story)

if __name__ == '__main':
    nurseryStories()