from unittest import TestCase
from factory.factory_method.stores.NYStylePizzaStore import NYStylePizzaStore


class TestNYStylePizzaStore(TestCase):

    def setUp(self) -> None:
        self.store = NYStylePizzaStore()

    def test_order_pizza(self):
        self.store.order_pizza('cheese')

