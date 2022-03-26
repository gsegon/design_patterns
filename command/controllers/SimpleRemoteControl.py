from command.commands.Command import Command


class SimpleRemoteControl:
    """ Simple Remote Control class (Invoker in the Command Pattern) """

    def __init__(self):
        """ Initializes the Simple Remote Control """
        self.slot = None

    def set_command(self, command: Command):
        """ Assigns the command to the slot """
        self.slot = command

    def button_was_pressed(self):
        """ Button was pressed """
        self.slot.execute()

