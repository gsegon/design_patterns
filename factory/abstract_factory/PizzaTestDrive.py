from factory.abstract_factory.stores.NYPizzaStore import NYPizzaStore
from factory.abstract_factory.stores.ChicagoPizzaStore import ChicagoPizzaStore


if __name__ == '__main__':
    nyStore = NYPizzaStore()
    chicagoStore = ChicagoPizzaStore()

    pizza = nyStore.order_pizza('veggie')
    print('Ethan ordered a ', pizza.get_name())
    print('')

    pizza = chicagoStore.order_pizza('veggie')
    print('Joel ordered a ', pizza.get_name())

