from command.commands.Command import Command
from command.vendors.CeilingFan import CeilingFan


class CeilingFanHighCommand(Command):
    """ Ceiling Fan High command """

    def __init__(self, ceiling_fan: CeilingFan):
        """Initialize with ceiling fan object"""
        self.prev_speed = None
        self.ceiling_fan = ceiling_fan

    def execute(self):
        """ Execute the command """
        self.prev_speed = self.ceiling_fan.get_speed()
        self.ceiling_fan.high()

    def undo(self):
        """ Undo the command """
        if self.prev_speed == CeilingFan.HIGH:
            self.ceiling_fan.high()
        elif self.prev_speed == CeilingFan.MEDIUM:
            self.ceiling_fan.medium()
        elif self.prev_speed == CeilingFan.LOW:
            self.ceiling_fan.low()
        elif self.prev_speed == CeilingFan.OFF:
            self.ceiling_fan.off()

