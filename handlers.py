# KeyError - EXAMPLE
def handle_key_error():
    fruit_prices = {'orange': 1.24, 'apple': 0.9}
    chosen_fruit = input("Which fruit would you like? ").strip().casefold()

    # Since the following line could cause an exception, wrap it in a try/except block:
    try:
        print(f"That will be {fruit_prices[chosen_fruit]}, please!")
    except KeyError:
        print("Sorry, we don't stock that fruit.")


# IndexError
def handle_index_error():
    options = ['Purchase some fruit', 'Find out more about the fruit we sell', 'Just have a browse']
    print("Welcome to the greengrocer's store! Your options:")
    for index, option in enumerate(options):
        print(f"{index}. {option}")
    chosen_option = input("Which option will you choose? Type its number: ").strip().casefold()

    # The following line could cause an exception:
    print(f"You selected: {options[int(chosen_option)]}.")
    # If there is an IndexError, print "Sorry, that isn't one of the available options."
    # Bonus: if there is a ValueError, catch that too in the same except block
    # Extra bonus: think of some way of writing the code so that a ValueError is never raised


# ValueError
def handle_value_error():
    orange_cost = 1.24
    orange_count = input("How many oranges would you like? ")

    # The following line could cause an exception:
    print(f"That will be {int(orange_count) * orange_cost}, please!")
    # If there is a ValueError, print "Sorry, that isn't a whole number of oranges."


# ZeroDivisionError
def handle_zero_division_error():
    orange_count = 1000
    print(f"Congratulations, one of you is the 1000th visitor to our store! You have won {orange_count} free oranges.")
    visitor_count = input("How many of you will be sharing the oranges? ")

    # The following line could cause an exception:
    print(f"In that case, each of you should receive {round(orange_count / int(visitor_count))} oranges.")
    # If there is a ZeroDivisionError, print "Sorry, we can't split the oranges between no people."
    # Bonus: if there is any other ValueError, print "Sorry, that isn't a whole number of people."


# FileNotFoundError
def handle_file_not_found_error():
    print("Thanks for placing an order with us!")
    filename = input("What is the name of your order file? ")

    # The following line could cause an exception:
    with open(filename, 'r'):
        print("Thanks, order received!")
    # If there is a FileNotFoundError, print "Sorry, we couldn't open your order file."
    # Bonus: if there is an IsADirectoryError, catch that too in the same block
    # Extra bonus: can you think of any other errors with opening the file that you could handle in the same block?


# UnicodeEncodeError
def handle_unicode_encode_error():
    print("Your friend has nominated you for a birthday gift!")
    print("It is a birthday orange engraved with a printable character of your choice (it should probably be ASCII...)")
    character = input("Which character would you like? ")

    with open('orange', 'wb') as orange_file:
        # The following line could cause an exception:
        orange_file.write(f" .oOOOo. \nd8     8b\n88  {character}  88\n88     88\n ^8bod8^ ".encode('ASCII'))
        print("Your orange is ready. Look around in your current folder!")
        # If there is a UnicodeEncodeError, print "Sorry, the character you chose wasn't ASCII."
