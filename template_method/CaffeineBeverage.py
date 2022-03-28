from abc import abstractmethod


class CaffeineBeverage:

    @abstractmethod
    def prepare_recipe(self):
        pass

    def boil_water(self):
        print('Boiling the water')

    def pour_in_cup(self):
        print('Pouring in cup')