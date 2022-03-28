from abc import ABC, abstractmethod


class CaffeineBeverageWithHook(ABC):
    """ CaffeineBeverage parent class """

    def prepare_recipe(self):
        """ Prepare the beverage """
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()

    def boil_water(self):
        """ Boil the water """
        print('Boiling the water')

    @abstractmethod
    def brew(self):
        """ Brew the beverage """
        pass

    def pour_in_cup(self):
        """ Pour the beverage in the cup """
        print('Pouring in cup')

    @abstractmethod
    def add_condiments(self):
        """ Add condiments to the beverage """
        pass

    def customer_wants_condiments(self):
        """ Returns True if customer wants condiments, otherwise False """
        return True

