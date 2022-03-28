from template_method.CaffeineBeverage import CaffeineBeverage


class Tea(CaffeineBeverage):

    def prepare_recipe(self):
        self.boil_water()
        self.steep_tea_bag()
        self.pour_in_cup()
        self.add_lemon()

    def steep_tea_bag(self):
        print('Steeping the Tea')

    def add_lemon(self):
        print('Adding Lemon')
