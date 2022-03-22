from command.commands.Command import Command
from command.vendors.Light import Light


class LightOnCommand(Command):
    """ Light On command """

    def __init__(self, light: Light):
        """Initialize with light object"""
        self.light = light

    def execute(self):
        """ Execute the LightOnCommand """
        self.light.on()

    def undo(self):
        """ Undo the LightOnCommand """
        self.light.off()
