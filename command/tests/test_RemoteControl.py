from unittest import TestCase
from command.RemoteControl import RemoteControl
from command.vendors.Light import Light
from command.vendors.Stereo import Stereo
from command.vendors.CeilingFan import CeilingFan
from command.commands.LightOnCommand import LightOnCommand
from command.commands.LightOffCommand import LightOffCommand
from command.commands.StereoWithCDCommand import StereoWithCDCommand
from command.commands.StereoOffCommand import StereoOffCommand
from command.commands.CeilingFanOnCommand import CeilingFanOnCommand
from command.commands.CeilingFanOffCommand import CeilingFanOffCommand
from command.commands.GarageDoorOpenCommand import GarageDoorOpen
from command.commands.GarageDoorCloseCommand import GarageDoorClose


class TestRemoteControl(TestCase):

    def setUp(self) -> None:
        """ SetUp the test class"""

        ''' Instantiate the RemoteControl '''
        self.remote = RemoteControl()

        ''' Setup receivers '''
        self.living_room_light = Light('Living Room')
        self.kitchen_light = Light('Kitchen')
        self.ceiling_fan = CeilingFan('Living Room')
        self.stereo = Stereo('Living Room')

        ''' Setup commands '''
        self.living_room_light_on_cmd = LightOnCommand(self.living_room_light)
        self.living_room_light_off_cmd = LightOffCommand(self.living_room_light)
        self.kitchen_light_on_cmd = LightOnCommand(self.kitchen_light)
        self.kitchen_light_off_cmd = LightOffCommand(self.kitchen_light)
        self.ceiling_fan_on_cmd = CeilingFanOnCommand(self.ceiling_fan)
        self.ceiling_fan_off_cmd = CeilingFanOffCommand(self.ceiling_fan)
        self.stereo_on_with_cd_cmd = StereoWithCDCommand(self.stereo)
        self.stereo_off_cmd = StereoOffCommand(self.stereo)

        ''' Assign commands to slots '''
        self.remote.set_command(0, self.living_room_light_on_cmd, self.living_room_light_off_cmd)
        self.remote.set_command(1, self.kitchen_light_on_cmd, self.kitchen_light_off_cmd)
        self.remote.set_command(2, self.ceiling_fan_on_cmd, self.ceiling_fan_off_cmd)
        self.remote.set_command(3, self.stereo_on_with_cd_cmd, self.stereo_off_cmd)

        ''' Print remote '''
        print(self.remote)

    def test_on_button_was_pressed(self):
        """ Test the On buttons """

        self.remote.on_button_was_pressed(0)
        self.remote.on_button_was_pressed(1)
        self.remote.on_button_was_pressed(2)
        self.remote.on_button_was_pressed(3)

        self.assertTrue(True)

    def test_off_button_was_pressed(self):
        """ Test the Off buttons """

        self.remote.off_button_was_pressed(0)
        self.remote.off_button_was_pressed(1)
        self.remote.off_button_was_pressed(2)
        self.remote.off_button_was_pressed(3)

        self.assertTrue(True)

    def test_slot_0(self):
        """ Test slot 0 """
        self.remote.on_button_was_pressed(0)
        self.remote.off_button_was_pressed(0)

    def test_slot_1(self):
        """ Test slot 1 """
        self.remote.on_button_was_pressed(1)
        self.remote.off_button_was_pressed(1)

    def test_slot_2(self):
        """ Test slot 2 """
        self.remote.on_button_was_pressed(2)
        self.remote.off_button_was_pressed(2)

    def test_slot_3(self):
        """ Test slot 3 """
        self.remote.on_button_was_pressed(3)
        self.remote.off_button_was_pressed(3)

    def test_undo(self):
        """ Test undo """
        self.remote.on_button_was_pressed(0)
        self.remote.off_button_was_pressed(0)
        print(self.remote)
        self.remote.undo_button_was_pressed()
        self.remote.off_button_was_pressed(0)
        self.remote.on_button_was_pressed(0)
        print(self.remote)
        self.remote.undo_button_was_pressed()

