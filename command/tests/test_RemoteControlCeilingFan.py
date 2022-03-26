from unittest import TestCase
from command.controllers.RemoteControl import RemoteControl
from command.vendors.CeilingFan import CeilingFan
from command.commands.CeilingFanOnCommand import CeilingFanOnCommand
from command.commands.CeilingFanOffCommand import CeilingFanOffCommand
from command.commands.CeilingFanMediumCommand import CeilingFanMediumCommand
from command.commands.CeilingFanHighCommand import CeilingFanHighCommand


class TestRemoteControlCeilingFan(TestCase):

    def setUp(self) -> None:
        """ SetUp the test class"""

        ''' Instantiate the RemoteControl '''
        self.remote = RemoteControl()

        ''' Setup receivers '''
        self.ceiling_fan = CeilingFan('Living Room')

        ''' Setup commands '''

        self.ceiling_fan_on_cmd = CeilingFanOnCommand(self.ceiling_fan)
        self.ceiling_fan_off_cmd = CeilingFanOffCommand(self.ceiling_fan)
        self.ceiling_fan_medium_cmd = CeilingFanMediumCommand(self.ceiling_fan)
        self.ceiling_fan_high_cmd = CeilingFanHighCommand(self.ceiling_fan)

        ''' Assign commands to slots '''
        self.remote.set_command(0, self.ceiling_fan_medium_cmd, self.ceiling_fan_off_cmd)
        self.remote.set_command(1, self.ceiling_fan_high_cmd, self.ceiling_fan_off_cmd)

        ''' Print remote '''
        print(self.remote)

    def test_on_button_was_pressed(self):
        """ Test the On buttons """

        self.remote.on_button_was_pressed(0)
        self.remote.on_button_was_pressed(1)

        self.assertTrue(True)

    def test_off_button_was_pressed(self):
        """ Test the Off buttons """

        self.remote.off_button_was_pressed(0)
        self.remote.off_button_was_pressed(1)

        self.assertTrue(True)

    def test_slot_0(self):
        """ Test slot 0 """
        self.remote.on_button_was_pressed(0)
        self.remote.off_button_was_pressed(0)

    def test_slot_1(self):
        """ Test slot 1 """
        self.remote.on_button_was_pressed(1)
        self.remote.off_button_was_pressed(1)

    def test_undo(self):
        """ Test undo """

        print('Undo command is: ', self.remote.undo_command)
        self.remote.on_button_was_pressed(0)
        print('')

        print('Undo command is: ', self.remote.undo_command)
        self.remote.off_button_was_pressed(0)
        print('')

        print('Undo command is: ', self.remote.undo_command)
        self.remote.undo_button_was_pressed()
        print('')

        print('Undo command is: ', self.remote.undo_command)
        self.remote.on_button_was_pressed(1)
        print('')

        print('Undo command is: ', self.remote.undo_command)
        self.remote.undo_button_was_pressed()
        print('')

        print('Undo command is: ', self.remote.undo_command)
        self.remote.undo_button_was_pressed()

        print('end')

