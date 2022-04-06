import unittest

from phonebook import PhoneBook


class PhoneBookTest(unittest.TestCase):
    def test_lookup_by_name(self):
        phonebook = PhoneBook()
        phonebook.add("Bob", "12345")
        number = phonebook.lookup("Bob")
        self.assertEqual("12345", number)
#Sample for testing
#        self.assertEqual(3,4)

# Main needs to be added for unitest pyhon -m unittest to pick up the test file.
# install the correct extension Python from Microsoft
if __name__ == '__main__':
    unittest.main()

