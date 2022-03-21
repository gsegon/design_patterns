from unittest import TestCase
from factory.factory_method.stores.ChicagoStylePizzaStore import ChicagoStylePizzaStore


class TestChicagoPizzaStore(TestCase):

    def setUp(self) -> None:
        self.store = ChicagoStylePizzaStore()

    def test_order_pizza(self):
        self.store.order_pizza('cheese')

