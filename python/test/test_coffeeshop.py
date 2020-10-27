from app import coffeeshop
import unittest

class MyTest(unittest.TestCase):
    def test_concrete_coffee(self):
        coffee = coffeeshop.Concrete_Coffee()

        self.assertEqual(coffee.get_cost(), 1.0)
        self.assertEqual(coffee.get_tax(), 0.1)
        self.assertEqual(coffee.get_ingredients(), "coffee")

    def test_coffee_with_sugar(self):
        coffee = coffeeshop.Concrete_Coffee()
        coffee_with_sugar = coffeeshop.Sugar(coffee)

        self.assertEqual(coffee_with_sugar.get_cost(), 1.0)
        self.assertEqual(coffee_with_sugar.get_tax(), 0.1)
        self.assertEqual(coffee_with_sugar.get_ingredients(), "coffee, sugar")

    def test_coffee_with_sugar_milk(self):
        coffee = coffeeshop.Concrete_Coffee()
        coffee_with_sugar = coffeeshop.Sugar(coffee)
        coffee_with_sugar_milk = coffeeshop.Milk(coffee_with_sugar)

        self.assertEqual(coffee_with_sugar_milk.get_cost(), 1.25)
        self.assertEqual(coffee_with_sugar_milk.get_tax(), 0.125)
        self.assertEqual(coffee_with_sugar_milk.get_ingredients(), "coffee, sugar, milk")

    def test_coffee_with_all(self):
        coffee = coffeeshop.Concrete_Coffee()
        coffee_with_sugar = coffeeshop.Sugar(coffee)
        coffee_with_sugar_milk = coffeeshop.Milk(coffee_with_sugar)
        coffee_with_all = coffeeshop.Vanilla(coffee_with_sugar_milk)

        self.assertEqual(coffee_with_all.get_cost(), 2.00)
        self.assertEqual(coffee_with_all.get_tax(), 0.2)
        self.assertEqual(coffee_with_all.get_ingredients(), "coffee, sugar, milk, vanilla")