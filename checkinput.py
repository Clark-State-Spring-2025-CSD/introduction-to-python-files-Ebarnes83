#Write a function that takes two parameters: a prompt message and an error message.
#The function will prompt the user with the passed in prompt to enter an integer
#If the text entered cannot be cast to an int, display the error message.
#The function will continue to prompt the user to enter an integer until a proper integer is entered.
#The most direct way of doing this would be using a try block, which has not been covered yet. You will need to research this.
#Write supporting code to call the function, and then display the number that was entered.

def get_integer_input(prompt_message, error_message):
    """
    Prompts the user for an integer input and handles potential conversion errors.

    Args:
        prompt_message (str): The message to display to the user.
        error_message (str): The message to display if the input is not an integer.

    Returns:
        int: The integer entered by the user.
    """
    while True:
        try:
            user_input = input(prompt_message)
            integer_value = int(user_input)
            return integer_value
        except ValueError:
            print(error_message)

prompt = "Please enter an integer: "
error = "Invalid integer. Please enter a valid integer."

number = get_integer_input(prompt, error)

print("You integer is:", number)