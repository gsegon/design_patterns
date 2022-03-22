from command.commands.Command import Command
from command.vendors.Stereo import Stereo


class StereoWithCDCommand(Command):
    """ StereoWithCD command """

    def __init__(self, stereo: Stereo):
        """ Initialize with Stereo """
        self.stereo = stereo

    def execute(self):
        """ Execute the command """
        self.stereo.on()
        self.stereo.set_cd()
        self.stereo.set_volume(11)
