

class Stereo:
    """ Stereo vendor class """

    def __init__(self, location):
        """ Initialize the Stereo """
        self.location = location
        self.volume = 0

    def on(self):
        """ Turns the stereo ON """
        print('Stereo ON')

    def off(self):
        """ Turns the stereo OFF"""
        print('Stereo OFF')

    def set_cd(self):
        """ Sets CD """
        print('Set CD')

    def set_dvd(self):
        """ Sets DVD """
        print('Set DVD')

    def set_radio(self):
        """ Sets Radio """
        print('Set Radio')

    def set_volume(self, volume):
        """ Sets volume """
        print('Set Volume to ', volume)
        self.volume = volume
