from factory.factory_method.stores.PizzaStore import PizzaStore
from factory.factory_method.pizzas import Pizza
from factory.factory_method.pizzas.california.CaliforniaStyleCheesePizza import CaliforniaStyleCheesePizza
from factory.factory_method.pizzas.california.CaliforniaStylePepperoniPizza import CaliforniaStylePepperoniPizza
from factory.factory_method.pizzas.california.CaliforniaStyleClamPizza import CaliforniaStyleClamPizza
from factory.factory_method.pizzas.california.CaliforniaStyleVeggiePizza import CaliforniaStyleVeggiePizza


class CaliforniaStylePizzaStore(PizzaStore):
    """ Classes that produce products are called concrete creators """

    def create_pizza(self, pizza_type: str) -> Pizza:
        """ This is our factory method implemented """

        pizza = None

        if pizza_type == 'cheese':
            pizza = CaliforniaStyleCheesePizza()
        elif pizza_type == 'pepperoni':
            pizza = CaliforniaStylePepperoniPizza()
        elif pizza_type == 'clam':
            pizza = CaliforniaStyleClamPizza()
        elif pizza_type == 'veggie':
            pizza = CaliforniaStyleVeggiePizza()

        return pizza
