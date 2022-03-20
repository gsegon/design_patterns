from unittest import TestCase
from PizzaStore import PizzaStore


class TestPizzaStore(TestCase):

    def setUp(self) -> None:
        self.store = PizzaStore()

    def test_order_pizza(self):
        self.store.order_pizza('pepperoni')

