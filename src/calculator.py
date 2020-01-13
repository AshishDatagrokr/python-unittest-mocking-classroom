from unittest import TestCase
from unittest.mock import patch
from src.calculator import Calculator

class TestCalculator(TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_sum_without_mocking(self):
        calculator = Calculator()
        actual = calculator.sum(2, 4)
        self.assertEqual(6, actual)

    @patch('src.calculator.Calculator')
    def test_sum_with_mocking(self, MockCalculator):
        calculator = MockCalculator() 

               calculator.sum.return_value = 6  

        actual = calculator.sum(2, 4)  
        expected = 6
        
        self.assertEqual(expected, actual)

        
        calculator.sum.return_value = 10
        actual = calculator.sum(1, 1)
        expected = 0
        self.assertEqual(expected, actual)
