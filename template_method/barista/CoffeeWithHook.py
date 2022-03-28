from template_method.barista.CaffeineBeverageWithHook import CaffeineBeverageWithHook


class CoffeeWithHook(CaffeineBeverageWithHook):
    """Coffee - inherits from CaffeineBeverage """

    def brew(self):
        """ Brew the Coffee """
        print('Dripping coffee through filter')

    def add_condiments(self):
        """ Add condiments """
        print('Adding sugar and milk')

    def customer_wants_condiments(self):
        answer = self.get_user_input()

        if answer == 'yes':
            return True
        else:
            return False

    def get_user_input(self):
        answer = input('Would you like milk and sugar with your coffee (y/n)?\n').lower()

        if (answer == 'y') or (answer == 'yes'):
            answer = 'yes'
        else:
            answer = 'no'

        return answer





