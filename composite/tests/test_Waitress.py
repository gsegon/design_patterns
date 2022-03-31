from unittest import TestCase
from composite.Waitress import Waitress
from composite.components.Menu import Menu
from composite.components.MenuItem import MenuItem


class TestWaitress(TestCase):

    def setUp(self) -> None:
        """ SetUp the test Waitress """

        ''' Initialize the Menus '''
        pancake_house_menu = Menu("PANCAKE HOUSE MENU", "Breakfast")
        diner_menu = Menu("DINER MENU", "Lunch")
        cafe_menu = Menu("CAFE MENU", "Dinner")
        dessert_menu = Menu("DESSERT MENU", "Dessert!")

        all_menus = Menu("ALL MENUS", "All menus combined")
        all_menus.add(pancake_house_menu)
        all_menus.add(diner_menu)
        all_menus.add(cafe_menu)
        all_menus.add(dessert_menu)

        ''' MenuItems of the pancake house menu '''
        pancake_house_menu.add(MenuItem("K&B\'s Pancake Breakfast",
                                        "Pancakes with scrambled eggs and toast",
                                        True,
                                        2.99))

        pancake_house_menu.add(MenuItem("Regular Pancake Breakfast",
                                        "Pancakes with fried eggs, sausage",
                                        False,
                                        2.99))

        pancake_house_menu.add(MenuItem("Blueberry Pancakes",
                                        "Pancakes made with fresh Blueberries",
                                        True,
                                        3.49))

        pancake_house_menu.add(MenuItem("Waffles",
                                        "Waffles with your choice of blueberries or strawberries",
                                        True,
                                        3.59))

        ''' MenuItems of the Diner menu '''
        diner_menu.add(MenuItem("Vegetarian BLT",
                                "(Fakin') Bacon with lettuce & tomato on whole wheat",
                                True,
                                2.99))

        diner_menu.add(MenuItem("BLT",
                                "Bacon with lettuce & tomato on whole wheat",
                                True,
                                2.99))

        diner_menu.add(MenuItem("Soup of the day",
                                "Soup of the day, with a side of potato salad",
                                False,
                                3.29))

        diner_menu.add(MenuItem("Hotdog",
                                "A hot dog, with sauerkraut, relish, onions, topped with cheese",
                                False,
                                3.05))

        ''' MenuItems of the Cafe menu and desert '''
        cafe_menu.add(MenuItem("Veggie Burger and Air Fries",
                               "Veggie burger on a whole wheat bun, lettuce, tomato, and fries",
                               True,
                               3.99))

        cafe_menu.add(MenuItem("Soup of the day",
                               "A cup of the soup of the day, with a side salad",
                               False,
                               3.69))

        cafe_menu.add(MenuItem("Burrito",
                               "A large burrito, with whole pinto beans, salsa, guacamole ",
                               True,
                               4.29))

        ''' Dessert menu (sub-menu of Cafe Menu)  '''
        dessert_menu.add(MenuItem("Apple Pie",
                                  "Apple pie with a flakey crust, topped with vanilla icecream",
                                  True,
                                  1.59))

        dessert_menu.add(MenuItem("Cheesecake",
                                  "Creamy New York cheesecake, with a chocolate graham crust",
                                  True,
                                  1.99))
        dessert_menu.add(MenuItem("Sorbet",
                                  "A scoop of raspberry and a scoop of lime",
                                  True,
                                  1.89))

        self.waitress = Waitress(all_menus)

    def test_print_menu(self):
        self.waitress.print_menu()
