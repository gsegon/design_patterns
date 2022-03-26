

class Hottub:
    """ Hottub vendor class """

    def __init__(self):
        """ Initializes the Hottub """
        self.temperature = 20   # degC

    def on(self):
        """ Turns the Hottub on """
        print('Hottub ON')

    def off(self):
        """ Turns the Hottub off """
        print('Hottub OFF')

    def circulate(self):
        """ Turns the water circulation """
        print('Hottub is circulating.')

    def jets_on(self):
        """ Turns the jets on """
        print('Hottub jets are ON.')

    def jets_off(self):
        """ Turns the jets on """
        print('Hottub jets are OFF.')

    def set_temperature(self, temperature):
        """ Set the Hottub temperature """
        self.temperature = temperature
        print('Hottub temperature set to ', self.temperature, ' degC.')
