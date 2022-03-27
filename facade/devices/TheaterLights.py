

class TheaterLights:
    """ TheaterLights device class """

    def on(self):
        """ Turn the lights on """
        print("The theater lights are ON")

    def off(self):
        """ Turn the lights off """
        print('he theater lights are OFF')

    def dim(self, level: int):
        """ Dim the lights """
        print('Dimming the lights to ', level, '%')
