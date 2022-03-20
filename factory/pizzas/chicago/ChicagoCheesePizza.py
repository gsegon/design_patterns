from factory.pizzas.Pizza import Pizza


class ChicagoCheesePizza(Pizza):
    """ A concrete product """

    def __init__(self):
        super(ChicagoCheesePizza, self).__init__()

        self.name = 'Chicago Style Deep Dish Cheese Pizza'
        self.dough = 'Extra Thick Crust Dough'
        self.sauce = 'Plum Tomato Sauce'
        self.toppings.append('Shredded Mozzarella Cheese')

    def cut(self):
        print('Cutting the pizza into square slices')
