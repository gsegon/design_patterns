# from facade.devices.Amplifier import Amplifier


class Tuner:
    """ Tuner device class """

    def __init__(self, amplifier):
        self.amplifier = amplifier
        self.frequency = 101.5      # MHz

    def on(self):
        """ Turn the tuner ON """
        print("The tuner is ON")

    def off(self):
        """ Turn the tuner OFF """
        print('The tuner is OFF')

    def set_am(self):
        """ Set to AM frequency """
        print('Tuner is set to AM')

    def set_fm(self):
        """ Set to FM frequency """
        print('Tuner is set to FM')

    def set_frequency(self, frequency: float):
        """ Set frequency """
        self.frequency = frequency

