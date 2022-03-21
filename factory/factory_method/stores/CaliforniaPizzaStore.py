from factory.factory_method.stores.PizzaStore import PizzaStore
from factory.factory_method.pizzas import Pizza
from factory.factory_method.pizzas.california.CaliforniaCheesePizza import CaliforniaCheesePizza
from factory.factory_method.pizzas.california.CaliforniaPepperoniPizza import CaliforniaPepperoniPizza
from factory.factory_method.pizzas.california.CaliforniaClamPizza import CaliforniaClamPizza
from factory.factory_method.pizzas.california.CaliforniaVeggiePizza import CaliforniaVeggiePizza


class CaliforniaPizzaStore(PizzaStore):
    """ Classes that produce products are called concrete creators """

    def create_pizza(self, pizza_type: str) -> Pizza:
        """ This is our factory method implemented """

        pizza = None

        if pizza_type == 'cheese':
            pizza = CaliforniaCheesePizza()
        elif pizza_type == 'pepperoni':
            pizza = CaliforniaPepperoniPizza()
        elif pizza_type == 'clam':
            pizza = CaliforniaClamPizza()
        elif pizza_type == 'veggie':
            pizza = CaliforniaVeggiePizza()

        return pizza
