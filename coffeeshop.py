class Abstract_Coffee():
    """
    The Base component interface defines operations that can be
    altered by decorators.
    """

    def get_cost(self) -> float:
        pass

    def get_ingredients(self) -> str:
        pass

    def get_tax(self) -> float:
        return 0.1 * self.get_cost()

class Concrete_Coffe(Abstract_Coffee):
    """
    Concrete component provide default implementations of the operations.
    """

    def get_cost(self) -> float:
        return 1.00

    def get_ingredients(self) -> str:
        return 'coffee'

class Abstract_Coffee_Decorator(Abstract_Coffee):
    """

    """

    def __init__(self, decorated_coffee):
        self.decorated_coffee = decorated_coffee

    def get_cost(self) -> float:
        return self.decorated_coffee.get_cost()

    def get_ingredients(self) -> str:
        return self.decorated_coffee.get_ingredients()

class Sugar(Abstract_Coffee_Decorator):
    """

    """

    def __init__(self, decorated_coffee):
        super(self, decorated_coffee)

    def get_cost(self) -> float:
        return self.decorated_coffee.get_cost()

    def get_ingredients(self) -> str:
        return self.decorated_coffee.get_ingredients() + ', sugar'

class Milk(Abstract_Coffee_Decorator):
    """

    """

    def __init__(self, decorated_coffee):
        super(self, decorated_coffee)

    def get_cost(self) -> float:
        return self.decorated_coffee.get_cost() + 0.25

    def get_ingredients(self) -> str:
        return self.decorated_coffee.get_ingredients() + ', milk'

class Vanilla(Abstract_Coffee_Decorator):
    """

    """

    def __init__(self, decorated_coffee):
        super(self, decorated_coffee)

    def get_cost(self) -> float:
        return self.decorated_coffee.get_cost() + 0.75

    def get_ingredients(self) -> str:
        return self.decorated_coffee.get_ingredients() + ', vanilla'
    