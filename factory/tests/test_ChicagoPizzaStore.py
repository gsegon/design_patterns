from unittest import TestCase
from factory.stores.ChicagoPizzaStore import ChicagoPizzaStore


class TestChicagoPizzaStore(TestCase):

    def setUp(self) -> None:
        self.store = ChicagoPizzaStore()

    def test_order_pizza(self):
        self.store.order_pizza('cheese')

