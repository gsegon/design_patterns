from command.commands.NoCommand import NoCommand
from command.commands.Command import Command


class RemoteControl:
    """ Remote Control class (Invoker in the Command Pattern) """

    def __init__(self):
        """ Initializes the RemoteControl by filling slots with NoCommands  """
        self.on_commands = [NoCommand() for _ in range(7)]
        self.off_commands = [NoCommand() for _ in range(7)]

    def set_command(self, slot, on_command: Command, off_command: Command):
        """ Sets the on and off commands at the specified slot """
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_was_pressed(self, slot):
        """ On button was pressed """
        self.on_commands[slot].execute()

    def off_button_was_pressed(self, slot):
        """ Off button was pressed """
        self.off_commands[slot].execute()

    def __str__(self):
        """ String print out of the Remote Control """
        buffer = ''
        buffer += '\n------ Remote Control ------\n'
        for slot, (on_command, off_command) in enumerate(zip(self.on_commands, self.off_commands)):
            buffer += '[slot ' + str(slot) + '] ' + on_command.__class__.__name__ + '      ' + \
                      off_command.__class__.__name__ + '\n'

        return buffer

