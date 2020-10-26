import coffeeshop
import unittest

class MyTest(unittest.TestCase):
    def test_concrete_coffee(self):
        coffee = coffeeshop.Concrete_Coffee()

        self.assertEqual(coffee.get_cost(), 1.0)
        self.assertEqual(coffee.get_tax(), 0.1)
        self.assertEqual(coffee.get_ingredients(), "coffee")