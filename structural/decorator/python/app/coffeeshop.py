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


class Concrete_Coffee(Abstract_Coffee):
    """
    Concrete component provide default implementations of the operations.
    """

    def get_cost(self):
        return 1.00

    def get_ingredients(self):
        return 'coffee'


class Coffee_Decorator(Abstract_Coffee):
    """
    The base Decorator class follows the same interface as the other components.
    The primary purpose of this class is to define the wrapping interface for
    all concrete decoratos. The default implementation of the wrapping code
    might include a field for storing a wrapped component and the means to
    initialize it.
    """

    _decorated_coffee: Abstract_Coffee = None

    def __init__(self, decorated_coffee: Abstract_Coffee) -> None:
        self._decorated_coffee = decorated_coffee

    def get_cost(self) -> float:
        return self._decorated_coffee.get_cost()

    def get_ingredients(self) -> str:
        return self._decorated_coffee.get_ingredients()


class Sugar(Coffee_Decorator):
    """
    Concrete decorator call the wrapped object and alter its result in some way.
    """

    def get_cost(self):
        return self._decorated_coffee.get_cost()

    def get_ingredients(self):
        return self._decorated_coffee.get_ingredients() + ', sugar'


class Milk(Coffee_Decorator):
    """
    Concrete decorator call the wrapped object and alter its result in some way.
    """

    def get_cost(self):
        return self._decorated_coffee.get_cost() + 0.25

    def get_ingredients(self):
        return self._decorated_coffee.get_ingredients() + ', milk'


class Vanilla(Coffee_Decorator):
    """
    Concrete decorator call the wrapped object and alter its result in some way.
    """

    def get_cost(self):
        return self._decorated_coffee.get_cost() + 0.75

    def get_ingredients(self):
        return self._decorated_coffee.get_ingredients() + ', vanilla'

