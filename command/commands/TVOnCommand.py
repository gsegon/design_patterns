from command.commands.Command import Command
from command.vendors.TV import TV


class TVOnCommand(Command):
    """ TVOn Command """

    def __init__(self, tv: TV):
        """ Initialize """
        self.tv = tv

    def execute(self):
        """ Execute the command """
        self.tv.set_volume(20)
        self.tv.on()

    def undo(self):
        """ Undo the command """
        self.tv.off()
