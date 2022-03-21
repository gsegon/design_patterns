from factory.abstract_factory.pizzas.Pizza import Pizza
from factory.abstract_factory.ingredients import PizzaIngredientFactory


class CheesePizza(Pizza):
    """ A concrete product """

    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        super(CheesePizza, self).__init__()
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        """ CheesePizza is the client code of the abstract factory. It calls methods specified in the abstract factory
        PizzaIngredientFactory but of the concrete implementation of IngredientFactory constructed in the store """

        print('Preparing ', self.name)
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()


