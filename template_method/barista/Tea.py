from template_method.barista.CaffeineBeverage import CaffeineBeverage


class Tea(CaffeineBeverage):
    """ Tea inherits from CaffeineBeverage """

    def brew(self):
        """ Brew the Tea """
        print('Steeping the Tea')

    def add_condiments(self):
        """ Add Condiments """
        print('Adding Lemon')
