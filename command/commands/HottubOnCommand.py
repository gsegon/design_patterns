from command.commands.Command import Command
from command.vendors.Hottub import Hottub


class HottubOnCommand(Command):
    """ HottubOn Command """

    def __init__(self, hottub: Hottub):
        """ Initialize """
        self.hottub = hottub

    def execute(self):
        """ Execute the command """
        self.hottub.set_temperature(30)
        self.hottub.on()

    def undo(self):
        """ Undo the command """
        self.hottub.off()
