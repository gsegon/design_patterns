from factory.factory_method.stores.PizzaStore import PizzaStore
from factory.factory_method.pizzas import Pizza
from factory.factory_method.pizzas.chicago.ChicagoStyleCheesePizza import ChicagoStyleCheesePizza
from factory.factory_method.pizzas.chicago.ChicagoStylePepperoniPizza import ChicagoStylePepperoniPizza
from factory.factory_method.pizzas.chicago.ChicagoStyleClamPizza import ChicagoStyleClamPizza
from factory.factory_method.pizzas.chicago import ChicagoStyleVeggiePizza


class ChicagoStylePizzaStore(PizzaStore):
    """ Classes that produce products are called concrete creators """

    def create_pizza(self, pizza_type: str) -> Pizza:
        """ This is our factory method implemented """

        pizza = None

        if pizza_type == 'cheese':
            pizza = ChicagoStyleCheesePizza()
        elif pizza_type == 'pepperoni':
            pizza = ChicagoStylePepperoniPizza()
        elif pizza_type == 'clam':
            pizza = ChicagoStyleClamPizza()
        elif pizza_type == 'veggie':
            pizza = ChicagoStyleVeggiePizza()

        return pizza
