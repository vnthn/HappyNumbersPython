import unittest

def is_happy_number(x):
    if x == 1:
        return True
    
    
class MyTest(unittest.TestCase):
    def test_happy_number_function(self):
        self.assertTrue(is_happy_number(1))
        self.assertTrue(is_happy_number(7))
        self.assertTrue(is_happy_number(1000))
        self.assertFalse(is_happy_number(4))
        self.assertFalse(is_happy_number(0))
        self.assertFalse(is_happy_number(-1))

if __name__ == '__main__':
    unittest.main()