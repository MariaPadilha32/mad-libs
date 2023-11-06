"""
inport the necessary functions to make sure users
will not input incorrect information only alphabetic characters
or numeric characters only. 
"""
from utils import get_non_empty_input
from utils import get_numeric_input

def foodStories():
    number_food = str(get_numeric_input("Enter a Number: "))
    number1_food = str(get_numeric_input("Enter a Number: "))
    number2_food = str(get_numeric_input("Enter a Number: "))
    ingredient1_food = get_non_empty_input("Enter an Ingredient: ")
    ingredient2_food = get_non_empty_input("Enter an Ingredient: ")
    number3_food = str(get_numeric_input("Enter a Number: "))
    condiment_food = get_non_empty_input("Enter a Condiment: ")
    verb_food = get_non_empty_input("Enter a Verb: ")
    noun_food = get_non_empty_input("Enter a Noun: ")
    adjective_food = get_non_empty_input("Enter an Adjective: ")
    adjective1_food = get_non_empty_input("Enter an Adjective: ")
    noun1_food = get_non_empty_input("Enter a Noun: ")

    foodStories = {
        "guacamole_food": (
            "\nClassic Guacamole: \nIngredients:\n" + number_food + " ripe avocados \n"
            "1 small " + ingredient1_food + " , finely diced\n" + number1_food + " - " + number2_food + " cloves " + ingredient1_food + ", minced\n"
            "1-2 " + ingredient2_food + " diced\nJuice of " + number3_food + "  lime(s)\n "
            "" + condiment_food + " and pepper to taste\n...\nInstructions:\n"
            "Cut the avocados in half, " + verb_food + "  the pit, and scoop the flesh into a " + noun_food + "\n"
            "Mash the avocados with a fork until you reach your desired consistency (some prefer " + adjective_food + ", while others like it " + adjective1_food + ").\n"
            "Add the diced " + ingredient1_food + ", minced " + ingredient1_food + ", and diced " + ingredient2_food +".\n"
            "Squeeze the lime juice over the mixture and season with " + number3_food + " and pepper.\n"
            "Mix everything together and serve with " + noun1_food + " or as a topping for tacos.\n")
    }

    print(foodStories["guacamole_food"])


if __name__ == '__main__':
    foodStories()
