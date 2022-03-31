from composite.components.MenuComponent import MenuComponent


class Menu(MenuComponent):
    """ Represents an implementation of a Menu. """

    def __init__(self, name: str, description: str):
        """ Initialize the Menu with the name and a description and an empty collection to store MenuItems """
        self.name = name
        self.description = description
        self.menu_components = []

    def add(self, component: 'MenuComponent'):
        self.menu_components.append(component)

    def remove(self, component: 'MenuComponent'):
        self.menu_components.remove(component)

    def get_child(self, index: int) -> 'MenuComponent':
        return self.menu_components[index]

    def get_name(self) -> str:
        """ Returns the name """
        return self.name

    def get_description(self) -> str:
        return self.description

    def __str__(self) -> str:
        string = '\n' + self.get_name()
        string += ', ' + self.get_description() + '\n'
        string += '--------------------\n'

        for menu_component in self.menu_components:
            string += menu_component.__str__()

        return string
