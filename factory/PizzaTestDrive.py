from stores.NYStylePizzaStore import NYStylePizzaStore
from stores.ChicagoPizzaStore import ChicagoPizzaStore


if __name__ == '__main__':
    nyStore = NYStylePizzaStore()
    chicagoStore = ChicagoPizzaStore()

    pizza = nyStore.order_pizza('cheese')
    print('Ethan ordered a ', pizza.get_name())
    print('')

    pizza = chicagoStore.order_pizza('cheese')
    print('Joel ordered a ', pizza.get_name())

