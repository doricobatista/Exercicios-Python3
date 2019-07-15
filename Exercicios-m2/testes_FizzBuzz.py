import unittest
from FizzBuzz import robot

class FizzBuzzTest(unittest.TestCase):
    def teste_1(self):
        self.assertEqual(robot(1), '1')
        
        
    def teste_3(self):
        self.assertEqual(robot(3), 'Fizz')
        
        
    def teste_5(self):
        self.assertEqual(robot(5), 'Buzz')
        
        
    def teste_15(self):
        self.assertEqual(robot(15), 'FizzBuzz')
        
        
    def teste_30(self):
        self.assertEqual(robot(30), 'FizzBuzz')
        
                
    def teste_90(self):
        self.assertEqual(robot(90), 'FizzBuzz')
        
        
    def teste_99(self):
        self.assertEqual(robot(99), 'Fizz')
        
        
    def teste_100(self):
        self.assertEqual(robot(100), 'Buzz')
        
    