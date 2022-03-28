from template_method.barista.CaffeineBeverage import CaffeineBeverage


class Coffee(CaffeineBeverage):
    """Coffee - inherits from CaffeineBeverage """

    def brew(self):
        """ Brew the Coffee """
        print('Dripping coffee through filter')

    def add_condiments(self):
        """ Add condiments """
        print('Adding sugar and milk')