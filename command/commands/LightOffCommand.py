from command.commands.Command import Command
from command.vendors.Light import Light


class LightOffCommand(Command):
    """ Light Off command """

    def __init__(self, light: Light):
        """Initialize with light object"""
        self.light = light

    def execute(self):
        """ Execute the LightOffCommand """
        self.light.off()

    def undo(self):
        """ Undo the LightOffCommand """
        self.light.on()