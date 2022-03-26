from command.commands.Command import Command


class MacroCommand(Command):
    """ Implements a Macro Command. A macro command contains multiple commands """

    def __init__(self, commands):
        """ Initialize the MacroCommand """
        self.commands = commands

    def execute(self):
        """ Execute the commands """
        for command in self.commands:
            command.execute()

    def undo(self):
        """ Undo do macro command """
        for command in self.commands[::-1]:
            command.undo()
