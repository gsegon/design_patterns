from command.commands.Command import Command
from command.vendors.CeilingFan import CeilingFan


class CeilingFanOnCommand(Command):
    """ Ceiling Fan On command """

    def __init__(self, ceiling_fan: CeilingFan):
        """Initialize with ceiling fan object"""
        self.ceiling_fan = ceiling_fan

    def execute(self):
        """ Execute the command """
        self.ceiling_fan.low()

    def undo(self):
        """ Undo the command """
        self.ceiling_fan.off()
