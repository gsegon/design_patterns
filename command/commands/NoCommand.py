from command.commands.Command import Command


class NoCommand(Command):

    def __init__(self):
        pass

    def execute(self):
        print('Do nothing.')
