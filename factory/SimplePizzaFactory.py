from CheesePizza import CheesePizza
from ClamPizza import ClamPizza
from PepperoniPizza import PepperoniPizza
from VeggiePizza import VeggiePizza
from Pizza import Pizza


class SimplePizzaFactory:

    def create_pizza(self, pizza_type: str) -> Pizza:

        pizza = None

        if pizza_type == 'cheese':
            pizza = CheesePizza()
        elif pizza_type == 'pepperoni':
            pizza = PepperoniPizza()
        elif pizza_type == 'clam':
            pizza = ClamPizza
        elif pizza_type == 'veggie':
            pizza = VeggiePizza

        return pizza

