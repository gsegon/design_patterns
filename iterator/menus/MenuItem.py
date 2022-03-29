

class MenuItem:
    """ Implementation of a MenuItem """

    def __init__(self, name: str, description: str, vegetarian: bool, price: float):
        """ Initialize the item """
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def get_name(self) -> str:
        """ Return the name of the Menu Item """
        return self.name

    def get_description(self) -> str:
        """ Return the description of the Menu Item """
        return self.description

    def get_vegetarian(self) -> bool:
        """ Return the True if the Menu Item is vegetarian, otherwise False """
        return self.vegetarian

    def get_price(self) -> float:
        """ Return the price of the Menu Item """
        return self.price
