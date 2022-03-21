from unittest import TestCase
from factory.abstract_factory.stores.NYPizzaStore import NYPizzaStore


class TestNYStylePizzaStore(TestCase):

    def setUp(self) -> None:
        self.store = NYPizzaStore()

    def test_order_pizza(self):
        self.store.order_pizza('cheese')

