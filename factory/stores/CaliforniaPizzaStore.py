from factory.stores.PizzaStore import PizzaStore
from factory.pizzas.Pizza import Pizza
from factory.pizzas.california.CaliforniaCheesePizza import CaliforniaCheesePizza
from factory.pizzas.california.CaliforniaPepperoniPizza import CaliforniaPepperoniPizza
from factory.pizzas.california.CaliforniaClamPizza import CaliforniaClamPizza
from factory.pizzas.california.CaliforniaVeggiePizza import CaliforniaVeggiePizza


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
