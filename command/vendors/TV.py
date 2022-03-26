

class TV:
    """ TV vendor class """

    def __init__(self, location):
        """ Initialize the Stereo """
        self.location = location
        self.volume = 0

    def on(self):
        """ Turns the TV ON """
        self.volume = 20
        print('TV ON')

    def off(self):
        """ Turns the TV OFF"""
        self.volume = 0
        print('TV OFF')

    def set_volume(self, volume):
        """ Sets volume """
        print('Set Volume to ', volume)
        self.volume = volume
