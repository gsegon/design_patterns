from template_method.barista.CaffeineBeverageWithHook import CaffeineBeverageWithHook


class TeaWithHook(CaffeineBeverageWithHook):
    """ Tea inherits from CaffeineBeverage """

    def brew(self):
        """ Brew the Tea """
        print('Steeping the Tea')

    def add_condiments(self):
        """ Add Condiments """
        print('Adding Lemon')

    def customer_wants_condiments(self):
        answer = self.get_user_input()

        if answer == 'yes':
            return True
        else:
            return False

    def get_user_input(self):
        answer = input('Would you like lemon with your tea (y/n)?\n').lower()

        if (answer == 'y') or (answer == 'yes'):
            answer = 'yes'
        else:
            answer = 'no'

        return answer

