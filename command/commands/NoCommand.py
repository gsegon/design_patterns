from command.commands.Command import Command


class NoCommand(Command):
    """ Implements a NoCommand Command. Un-assigned slots are assigned a NoCommand rather then None """

    def execute(self):
        """ Executes the command - Does nothing """
        print('Do nothing.')

    def undo(self):
        """ Undoes the command - Does nothing """
        print('Do nothing')
