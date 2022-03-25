

class CeilingFan:
    """ Ceiling fan vendor class """

    ''' Speed settings '''
    HIGH = 3
    MEDIUM = 2
    LOW = 1
    OFF = 0

    def __init__(self, location):
        """ Initialize the CeilingFan """

        self.location = location
        self.speed = self.OFF

    def high(self):
        """ Set speed to high """
        self.speed = self.HIGH
        print(self.location, ' Ceiling Fan speed set to HIGH')

    def medium(self):
        """ Set speed to medium """
        self.speed = self.MEDIUM
        print(self.location, ' Ceiling Fan speed set to MEDIUM')

    def low(self):
        self.speed = self.LOW
        """ Set speed to low """
        print(self.location, ' Ceiling Fan speed set to LOW')

    def off(self):
        """ The the ceiling fan OFF """
        self.speed = self.OFF
        print(self.location, ' Ceiling Fan is OFF')

    def get_speed(self):
        """ get the current ceiling fan speed """
        return self.speed
