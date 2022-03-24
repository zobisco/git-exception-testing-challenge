from unittest import TestCase, main
import exceptions


# Test to make sure exceptions aren't arising directly from raise statements
class TestExceptionsFileContent(TestCase):

    def test_raise_keyword_not_used(self):
        with open('exceptions.py', 'r') as exceptions_file:
            exceptions_file_content = exceptions_file.read()
        raise_keyword_detected = 'raise' in exceptions_file_content.split()
        self.assertFalse(raise_keyword_detected, msg="Raise keyword detected in exceptions.py")


# Tests to make sure expected exceptions arise
class TestExceptions(TestCase):

    def test_produce_attribute_error(self):
        with self.assertRaises(AttributeError):
            exceptions.produce_attribute_error()

    def test_produce_key_error(self):
        with self.assertRaises(KeyError):
            exceptions.produce_key_error()

    def test_produce_index_error(self):
        with self.assertRaises(IndexError):
            exceptions.produce_index_error()

    def test_produce_name_error(self):
        with self.assertRaises(NameError):
            exceptions.produce_name_error()

    def test_produce_unbound_local_error(self):
        with self.assertRaises(UnboundLocalError):
            exceptions.produce_unbound_local_error()

    def test_produce_type_error(self):
        with self.assertRaises(TypeError):
            exceptions.produce_type_error()

    def test_produce_value_error(self):
        with self.assertRaises(ValueError):
            exceptions.produce_value_error()

    def test_produce_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError):
            exceptions.produce_zero_division_error()

    def test_produce_overflow_error(self):
        with self.assertRaises(OverflowError):
            exceptions.produce_overflow_error()

    def test_produce_file_not_found_error(self):
        with self.assertRaises(FileNotFoundError):
            exceptions.produce_file_not_found_error()

    def test_produce_unicode_encode_error(self):
        with self.assertRaises(UnicodeEncodeError):
            exceptions.produce_unicode_encode_error()

    def test_produce_module_not_found_error(self):
        with self.assertRaises(ModuleNotFoundError):
            exceptions.produce_module_not_found_error()

    def test_produce_import_error(self):
        with self.assertRaises(ImportError):
            exceptions.produce_import_error()


if __name__ == '__main__':
    main()
