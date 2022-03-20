from unittest import TestCase
from factory.stores.CaliforniaPizzaStore import CaliforniaPizzaStore


class TestNYStylePizzaStore(TestCase):

    def setUp(self) -> None:
        self.store = CaliforniaPizzaStore()

    def test_order_pizza(self):
        self.store.order_pizza('pepperoni')

