# BROAD REASONS WHY YOU MIGHT GET AN EXCEPTION
# (1) Trying to refer to something that doesn't exist
# (2) Using a value that is inappropriate in some way

# CORE EXAMPLES OF EXCEPTIONS IN THIS FILE
# AttributeError (1)
# KeyError (1)
# IndexError (1)
# NameError (1)
# UnboundLocalError (1)
# TypeError (2)
# ValueError (2)
# ZeroDivisionError (2)
# OverflowError (2)
# FileNotFoundError (1)
# UnicodeEncodeError (2)
# ModuleNotFoundError (1)
# ImportError (1)

# BONUS EXAMPLES YOU CAN TRY IF YOU WISH
# PermissionError (2)
# IsADirectoryError (2)


# AttributeError - EXAMPLE
def produce_attribute_error():
    print(1.234.upper())


# KeyError
def produce_key_error():
    ages = {'Aishat': 30, 'Zoe': 28, 'Alexis': 33}
    print(ages['Emily'])


# IndexError
def produce_index_error():
    my_list = [1, 2, 3, 4, 5]
    my_list[10]


# NameError
def produce_name_error():
    name = "Test"
    print(nmae)


# UnboundLocalError
def produce_unbound_local_error():
    print(x)
    x = 9


# TypeError
def produce_type_error():
    myInt = 100
    myStr = "10"
    myResult = myInt / myStr


# ValueError
def produce_value_error():
    new_variable = "Test"
    print(int(new_variable))


# ZeroDivisionError
def produce_zero_division_error():
    a = 10
    b = 0
    c = a/b


# OverflowError
def produce_overflow_error():
    # while True:
    #     print("test")
    pass


# FileNotFoundError
def produce_file_not_found_error():
    with open("READYOU.md", 'r') as file:
        file.write('Hi there!')


# UnicodeEncodeError
def produce_unicode_encode_error():
    f = open('demo.txt', 'w')
    f.write('να έχεις μια όμορφη μέρα')
    f.close()


# ModuleNotFoundError
def produce_module_not_found_error():
    import apple


# ImportError
def produce_import_error():
    from math import apple


# PermissionError
def produce_permission_error():
    pass


# IsADirectoryError
def produce_is_a_directory_error():
    pass