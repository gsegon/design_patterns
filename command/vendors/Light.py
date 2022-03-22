

class Light:
    """ Light vendor class """

    def __init__(self, location):
        """ Initializes the Light """
        self.location = location

    def on(self):
        """ Turns the light on """
        print(self.location + ' Light ON')

    def off(self):
        """ Turns the light off """
        print(self.location + ' Light OFF')
