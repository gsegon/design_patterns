from factory.factory_method.pizzas.Pizza import Pizza


class NYStyleCheesePizza(Pizza):
    """ A concrete product """

    def __init__(self):
        super(NYStyleCheesePizza, self).__init__()
        self.name = 'NY Style Sauce and Cheese Pizza'
        self.dough = 'Thin crust Dough'
        self.sauce = 'Marinara Sauce'
        self.toppings.append('Grated Reggiano Cheese')
