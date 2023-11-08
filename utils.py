def get_non_empty_input(prompt):
    """
    function created so all Input for nouns, names, colors,
    etc will accept only alphabetic characters.
    """
    while True:
        user_input = input(prompt)
        if user_input.isalpha():
            return user_input
        else:
            print("**Please enter a single word.**")


def get_numeric_input(prompt):
    """
    function created so all numeric inputs
    will accept only numbers.
    """
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print('**Please enter only integer numbers.**')
