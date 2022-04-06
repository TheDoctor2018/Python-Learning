import unittest


class PhoneBookTest(unittest.TestCase):
    def Test_lookup_by_name(self):
        phonebook = phonebook()
        phonebook.add("Bob", "12345")
        number = phonebook.lookup("Bob")
        self.assertEqual("12345", number)


# Main needs to be added for unitest pyhon -m unittest to pick up the test file.
# install the correct extension Python from Microsoft
if __name__ == '__main__':
    unittest.main()

