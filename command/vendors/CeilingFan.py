

class CeilingFan:
    """ Ceiling fan vendor class """

    def __init__(self, location):
        """ Initialize the CeilingFan """
        self.location = location
        self.speed = 0.0

    def high(self):
        """ Set speed to high """
        self.speed = 100
        print(self.location, ' Ceiling Fan speed set to HIGH')

    def medium(self):
        """ Set speed to medium """
        self.speed = 50
        print(self.location, ' Ceiling Fan speed set to MEDIUM')

    def low(self):
        self.speed = 20
        """ Set speed to low """
        print(self.location, ' Ceiling Fan speed set to LOW')

    def off(self):
        """ The the ceiling fan OFF """
        self.speed = 0
        print(self.location, ' Ceiling Fan is OFF')

    def get_speed(self):
        """ get the current ceiling fan speed """
        return self.speed
