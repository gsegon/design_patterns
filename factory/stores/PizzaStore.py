from abc import ABC, abstractmethod
from factory.pizzas.Pizza import Pizza


class PizzaStore(ABC):

    def order_pizza(self, pizza_type):

        pizza = self.create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    @abstractmethod
    def create_pizza(self, pizza_type: str) -> Pizza:
        pass
