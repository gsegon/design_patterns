from factory.factory_method.stores.PizzaStore import PizzaStore
from factory.factory_method.pizzas.Pizza import Pizza
from factory.factory_method.pizzas.new_york.NYStyleCheesePizza import NYStyleCheesePizza
from factory.factory_method.pizzas.new_york.NYStylePepperoniPizza import NYStylePepperoniPizza
from factory.factory_method.pizzas.new_york.NYStyleClamPizza import NYStyleClamPizza
from factory.factory_method.pizzas.new_york.NYStyleVeggiePizza import NYStyleVeggiePizza


class NYStylePizzaStore(PizzaStore):
    """ Classes that produce products are called concrete creators """

    def create_pizza(self, pizza_type: str) -> Pizza:
        """ This is our factory method implemented """

        pizza = None

        if pizza_type == 'cheese':
            pizza = NYStyleCheesePizza()
        elif pizza_type == 'pepperoni':
            pizza = NYStylePepperoniPizza()
        elif pizza_type == 'clam':
            pizza = NYStyleClamPizza()
        elif pizza_type == 'veggie':
            pizza = NYStyleVeggiePizza()

        return pizza
