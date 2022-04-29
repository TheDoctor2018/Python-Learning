import unittest
from zlib import DEF_BUF_SIZE

from phonebook import PhoneBook


class PhoneBookTest(unittest.TestCase):
    
    def setUp(self):
        self.phonebook =PhoneBook()
    
    def test_lookup_by_name(self):
        phonebook = PhoneBook()
        phonebook.add("Bob", "12345")
        number = phonebook.lookup("Bob")
        self.assertEqual("12345", number)
       
       
    def test_missing_name(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")
    
    #@unittest.skip("WIP")
    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())     
        
        
    #Poor Unit Test Design below.
    @unittest.skip("WIP")
    def test_is_consistent(self):
         self.phonebook.add("Bob", "12345")
         self.assertTrue(self.phonebook.is_consistent())     
         self.phonebook.add("ANNS", "267445")
         self.assertTrue(self.phonebook.is_consistent())          
         self.phonebook.add("AJan", "12345")
         self.assertFalse(self.phonebook.is_consistent())  
         self.phonebook.add("AJan", "123")#prefix of bob, should not be consistant
         self.assertFalse(self.phonebook.is_consistent())    
         
    #Arrange,Act,Assert better design for method body of tests from above
    #Allos for a fuller picture of what is working or not.
    def test_is_consistent_with_different_entries(self):
        self.phonebook.add("Bob", "12345")   
        self.phonebook.add("ANNS", "267445")
        self.assertTrue(self.phonebook.is_consistent())              

    def test_is_consistent_with_duplicate_entries(self):
        self.phonebook.add("Bob", "12345")   
        self.phonebook.add("Ajan", "12345")
        self.assertFalse(self.phonebook.is_consistent())       
        
    def test_is_consistent_with_duplicate_prefix(self):
        self.phonebook.add("Bob", "12345")   
        self.phonebook.add("Ajan", "123")
        self.assertFalse(self.phonebook.is_consistent())             
        
#Sample for testing
#        self.assertEqual(3,4)

#Need to check for consistancy
    #Number same as the other or prefix of another number?? How to check for this

# Main needs to be added for unitest pyhon -m unittest to pick up the test file.
# install the correct extension Python from Microsoft


