from unittest import TestCase, mock, main
from io import StringIO
import os
import handlers


# Helper function to get most recently printed line
def get_last_line(out):
    return out.getvalue().strip().splitlines()[-1]


# Helper function for FileNotFoundError tests
def remove_file_or_directory_if_exists(filename):
    try:
        os.remove(filename)  # Remove file if exists
        os.rmdir(filename)   # Remove directory (folder) if exists
    except OSError:
        pass


# Test to make sure exceptions aren't arising directly from raise statements
class TestHandlersFileContent(TestCase):

    def test_raise_keyword_not_used(self):
        with open('handlers.py', 'r') as exceptions_file:
            exceptions_file_content = exceptions_file.read()
        raise_keyword_detected = 'raise' in exceptions_file_content.split()
        self.assertFalse(raise_keyword_detected, msg="Raise keyword detected in handlers.py")


# Tests to make sure correct outputs arise from valid inputs
class TestHandlersWithValidInput(TestCase):

    def test_handle_key_error_with_valid_input(self):
        with mock.patch('builtins.input', return_value='orange'), mock.patch('sys.stdout', new=StringIO()) as out:
            handlers.handle_key_error()
            self.assertEqual(get_last_line(out), "That will be 1.24, please!")

    def test_handle_index_error_with_valid_input(self):
        with mock.patch('builtins.input', return_value='0'), mock.patch('sys.stdout', new=StringIO()) as out:
            handlers.handle_index_error()
            self.assertEqual(get_last_line(out), "You selected: Purchase some fruit.")

    def test_handle_value_error_with_valid_input(self):
        with mock.patch('builtins.input', return_value='2'), mock.patch('sys.stdout', new=StringIO()) as out:
            handlers.handle_value_error()
            self.assertEqual(get_last_line(out), "That will be 2.48, please!")

    def test_handle_zero_division_error_with_valid_input(self):
        with mock.patch('builtins.input', return_value='5'), mock.patch('sys.stdout', new=StringIO()) as out:
            handlers.handle_zero_division_error()
            self.assertEqual(get_last_line(out), "In that case, each of you should receive 200 oranges.")

    def test_handle_file_not_found_error_with_valid_input(self):
        this_file = os.path.basename(__file__)
        with mock.patch('builtins.input', return_value=this_file), mock.patch('sys.stdout', new=StringIO()) as out:
            handlers.handle_file_not_found_error()
            self.assertEqual(get_last_line(out), "Thanks, order received!")

    def test_handle_unicode_encode_error_with_valid_input(self):
        remove_file_or_directory_if_exists('orange')
        with mock.patch('builtins.input', return_value='E'), mock.patch('sys.stdout', new=StringIO()) as out:
            handlers.handle_unicode_encode_error()
            self.assertEqual(get_last_line(out), "Your orange is ready. Look around in your current folder!")
            with open('orange', 'r') as orange_file:
                self.assertEqual(orange_file.readlines(), [" .oOOOo. \n",
                                                           "d8     8b\n",
                                                           "88  E  88\n",
                                                           "88     88\n",
                                                           " ^8bod8^ "])


# Tests to make sure correct outputs arise from invalid inputs
class TestHandlersWithInvalidInput(TestCase):

    def test_handle_key_error_with_invalid_input(self):
        with mock.patch('builtins.input', return_value='banana'), mock.patch('sys.stdout', new=StringIO()) as out:
            handlers.handle_key_error()
            self.assertEqual(get_last_line(out), "Sorry, we don't stock that fruit.")

    def test_handle_index_error_with_out_of_range_input(self):
        with mock.patch('builtins.input', return_value='5'), mock.patch('sys.stdout', new=StringIO()) as out:
            handlers.handle_index_error()
            self.assertEqual(get_last_line(out), "Sorry, that isn't one of the available options.")

    def test_handle_value_error_with_invalid_input(self):
        with mock.patch('builtins.input', return_value='4.8'), mock.patch('sys.stdout', new=StringIO()) as out:
            handlers.handle_value_error()
            self.assertEqual(get_last_line(out), "Sorry, that isn't a whole number of oranges.")

    def test_handle_zero_division_error_with_zero_input(self):
        with mock.patch('builtins.input', return_value='0'), mock.patch('sys.stdout', new=StringIO()) as out:
            handlers.handle_zero_division_error()
            self.assertEqual(get_last_line(out), "Sorry, we can't split the oranges between no people.")

    def test_handle_file_not_found_error_with_invalid_input(self):
        remove_file_or_directory_if_exists('!@£$%^&*.txt')
        with mock.patch('builtins.input', return_value='!@£$%^&*.txt'), mock.patch('sys.stdout', new=StringIO()) as out:
            handlers.handle_file_not_found_error()
            self.assertEqual(get_last_line(out), "Sorry, we couldn't find your order file.")

    def test_handle_unicode_encode_error_with_valid_input(self):
        with mock.patch('builtins.input', return_value='£'), mock.patch('sys.stdout', new=StringIO()) as out:
            handlers.handle_unicode_encode_error()
            self.assertEqual(get_last_line(out), "Sorry, the character you chose wasn't ASCII.")


# Bonus tests to make sure correct outputs arise from invalid inputs
class TestHandlersWithBonusInvalidInput(TestCase):

    def test_handle_index_error_with_non_numeric_input(self):
        with mock.patch('builtins.input', return_value='Bungled'), mock.patch('sys.stdout', new=StringIO()) as out:
            handlers.handle_index_error()
            self.assertEqual(get_last_line(out), "Sorry, that isn't one of the available options.")

    def test_handle_zero_division_error_with_non_numeric_input(self):
        with mock.patch('builtins.input', return_value='Donkeys'), mock.patch('sys.stdout', new=StringIO()) as out:
            handlers.handle_zero_division_error()
            self.assertEqual(get_last_line(out), "Sorry, that isn't a whole number of people.")

    def test_handle_file_not_found_error_with_directory_input(self):
        remove_file_or_directory_if_exists('!@£$%^&*')
        # Make directory (folder) instead of file and perform test
        try:
            os.mkdir('!@£$%^&*')
            with mock.patch('builtins.input', return_value='!@£$%^&*'), mock.patch('sys.stdout', new=StringIO()) as out:
                handlers.handle_file_not_found_error()
                self.assertEqual(get_last_line(out), "Sorry, we couldn't find your order file.")
        finally:
            os.rmdir('!@£$%^&*')


if __name__ == '__main__':
    main()
