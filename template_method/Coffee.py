from template_method.CaffeineBeverage import CaffeineBeverage


class Coffee(CaffeineBeverage):

    def prepare_recipe(self):
        self.boil_water()
        self.brew_coffee_grinds()
        self.pour_in_cup()
        self.add_sugar_and_milk()

    def brew_coffee_grinds(self):
        print('Dripping coffee through filter')

    def add_sugar_and_milk(self):
        print('Adding sugar and milk')