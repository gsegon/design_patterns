from command.commands.Command import Command
from command.vendors.Stereo import Stereo


class StereoOffCommand(Command):
    """ StereoOff command """

    def __init__(self, stereo: Stereo):
        """ Initialize with Stereo """
        self.stereo = stereo

    def execute(self):
        """ Execute the command """
        self.stereo.off()
