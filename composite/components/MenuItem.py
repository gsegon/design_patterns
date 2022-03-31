from composite.components.MenuComponent import MenuComponent


class MenuItem(MenuComponent):
    """
    Represents a Menu Item. (Leaf in the context of a Composite pattern)
    """

    def __init__(self, name: str, description: str, vegetarian: bool, price: float):
        """ Initialize the MenuItem with name, description, vegetarian (bool), and a price. """
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def get_name(self) -> str:
        """ Returns the name """
        return self.name

    def get_description(self) -> str:
        """ Returns the description """
        return self.description

    def get_price(self) -> float:
        """ Returns the price """
        return self.price

    def is_vegetarian(self) -> bool:
        """ Returns True if vegetarian, otherwise false """
        return self.vegetarian

    def __str__(self):
        string = self.get_name()
        if self.is_vegetarian():
            string += '(v)'
        string += ', ' + str(self.get_price()) + '\n'
        string += '\t -- ' + self.get_description() + '\n'

        return string
