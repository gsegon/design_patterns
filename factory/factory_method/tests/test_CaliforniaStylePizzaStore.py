from unittest import TestCase
from factory.factory_method.stores.CaliforniaStylePizzaStore import CaliforniaStylePizzaStore


class TestCaliforniaStylePizzaStore(TestCase):

    def setUp(self) -> None:
        self.store = CaliforniaStylePizzaStore()

    def test_order_pizza(self):
        self.store.order_pizza('pepperoni')

