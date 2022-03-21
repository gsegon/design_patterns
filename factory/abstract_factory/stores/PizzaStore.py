from abc import ABC, abstractmethod
from factory.factory_method.pizzas.Pizza import Pizza


# This is our abstract creator class. It defines an abstract factory
# method that the subclasses implement to produce products
class PizzaStore(ABC):
    """
    This is our abstract creator class. It defines an abstract factory
    method that the subclasses implement to produce products.
    """

    def order_pizza(self, pizza_type):
        """
        Code that depends on an abstract product which is produced by a subclass.
        The creator never really knows which concrete product was produced
        """

        pizza = self.create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    @abstractmethod
    def create_pizza(self, pizza_type: str) -> Pizza:
        """ Factory method (abstract) """
        pass
