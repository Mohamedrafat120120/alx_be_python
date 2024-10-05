import unittest
from simple_calculator import SimpleCalculator

class test_calculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        result=self.calc.add(4,6)
        self.assertEqual(result,10)
        
    def test_subtraction(self):
        result=self.calc.subtract(4,2)
        self.assertEqual(result,2)
        
        
    def test_multiply(self):
        result=self.calc.multiply(6,6)
        self.assertEqual(result,36)
        
        
    def test_divide(self):
        result=self.calc.divide(4,2)
        self.assertEqual(result,2)
        
        
if __name__=="__main__":
    unittest.main()