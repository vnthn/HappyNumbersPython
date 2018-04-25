import unittest
def sum_of_square_of_digits_of(n):
   sum = 0
   while n:
      sum += (n % 10) * (n % 10)
      n = int(n/10)
   return sum
def is_happy_number(x):
    if (x <= 0) or (x == 4):
        return False
    y = sum_of_square_of_digits_of(x)
    if y == 1:
        return True
    else:
        is_happy_number(y)
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