from utils import get_non_empty_input
from utils import get_numeric_input

def randStories():
    silly_word_random = get_non_empty_input("Enter a Silly Word: ")
    surname_random = get_non_empty_input("Enter a Surname: ")
    illness_random = get_non_empty_input("Enter an Illness: ")
    noun_plural_random = get_non_empty_input("Enter a Noun (Plural): ")
    adjective_random = get_non_empty_input("Enter an Adjective: ")
    adjective1_random = get_non_empty_input("Enter an Adjective: ")
    silly2_word_random = get_non_empty_input("Enter a Silly Word: ")
    place_random = get_non_empty_input("Enter a Place: ")
    number_random = str(get_numeric_input("Enter a Number: "))
    adjective2_random = get_non_empty_input("Enter an Adjective: ")

    sick_note = (
        "\nDear School Nurse:\n" + silly_word_random + " " + surname_random + " will not be attending school today.\n"
        "He/she has come down with a case of " + illness_random + " and has horrible " + noun_plural_random + " and a/an " + adjective_random + " fever.\n"
        "We have made an appointment with the " + adjective1_random + " Dr. " + silly2_word_random + ",\n"
        "who studied for many years in " + place_random + " and has " + number_random + " degrees in pediatrics.\n"
        "He will send you all the information you need.\nThank you!\nSincerely,\nMrs. " + adjective2_random + ".\n"
    )
    print(sick_note)


if __name__ == '__main__':
    randStories()