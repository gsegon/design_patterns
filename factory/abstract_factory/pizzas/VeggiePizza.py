from factory.abstract_factory.pizzas.Pizza import Pizza
from factory.abstract_factory.ingredients import PizzaIngredientFactory


class VeggiePizza(Pizza):
    """ A concrete product """

    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        super(VeggiePizza, self).__init__()
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print('Preparing ', self.name)
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.veggies = self.ingredient_factory.create_veggies()



