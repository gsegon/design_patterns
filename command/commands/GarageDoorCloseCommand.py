from command.commands.Command import Command
from command.vendors.GarageDoor import GarageDoor


class GarageDoorClose(Command):
    """ GarageDoorClose command"""

    def __init__(self, garage_door: GarageDoor):
        """ Initialize with GarageDoor object """
        self.garage_door = garage_door

    def execute(self):
        """ Execute the command """
        self.garage_door.light_off()
        self.garage_door.down()

    def undo(self):
        """ Undo the command """
        self.garage_door.up()
        self.garage_door.light_on()

