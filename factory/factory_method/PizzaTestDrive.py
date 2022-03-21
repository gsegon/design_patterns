from factory.factory_method.stores.NYStylePizzaStore import NYStylePizzaStore
from factory.factory_method.stores.ChicagoStylePizzaStore import ChicagoStylePizzaStore


if __name__ == '__main__':
    nyStore = NYStylePizzaStore()
    chicagoStore = ChicagoStylePizzaStore()

    pizza = nyStore.order_pizza('cheese')
    print('Ethan ordered a ', pizza.get_name())
    print('')

    pizza = chicagoStore.order_pizza('cheese')
    print('Joel ordered a ', pizza.get_name())

