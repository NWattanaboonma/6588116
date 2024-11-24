import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(45, 75), 120)
    # Add the following test methods to the TestCalculator class:

    def test_sub(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)
        self.assertEqual(self.calc.subtract(1, 2), -1)
    
    def test_muti(self):
        self.assertEqual(self.calc.multiply(2, 1), 2)
        self.assertEqual(self.calc.multiply(1, 132), 132)
        self.assertEqual(self.calc.multiply(-1, 132), -132)
        self.assertEqual(self.calc.multiply(1, -132), -132)
        self.assertEqual(self.calc.multiply(-1, -132), 132)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(2,5),0)
        self.assertEqual(self.calc.divide(1000,3),333)
        self.assertEqual(self.calc.divide(1000,-3),-333)
        self.assertEqual(self.calc.divide(-1000,-3),333)


    def test_mod(self):
        self.assertEqual(self.calc.modulo(4,4),0)
        self.assertEqual(self.calc.modulo(4,5),4)
        self.assertEqual(self.calc.modulo(4,6),4)
       


if __name__ == '__main__':
    unittest.main()