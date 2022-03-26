from unittest import TestCase
from command.controllers.RemoteControl import RemoteControl

from command.vendors.Light import Light
from command.vendors.Stereo import Stereo
from command.vendors.TV import TV
from command.vendors.Hottub import Hottub

from command.commands.LightOnCommand import LightOnCommand
from command.commands.LightOffCommand import LightOffCommand
from command.commands.StereoWithCDCommand import StereoWithCDCommand
from command.commands.StereoOffCommand import StereoOffCommand
from command.commands.TVOnCommand import TVOnCommand
from command.commands.TVOffCommand import TVOffCommand
from command.commands.HottubOnCommand import HottubOnCommand
from command.commands.HottubOffCommand import HottubOffCommand
from command.commands.MacroCommand import MacroCommand


class TestPartyMode(TestCase):

    def setUp(self) -> None:
        """ SetUp the test class"""

        ''' Instantiate the RemoteControl '''
        self.remote = RemoteControl()

        ''' Setup receivers '''
        living_room_light = Light('Living Room')
        living_room_stereo = Stereo('Living Room')
        living_room_tv = TV('Living Room')
        hottub = Hottub()

        ''' Setup commands '''
        living_room_light_on_cmd = LightOnCommand(living_room_light)
        living_room_light_off_cmd = LightOffCommand(living_room_light)

        stereo_on_with_cd_cmd = StereoWithCDCommand(living_room_stereo)
        stereo_off_cmd = StereoOffCommand(living_room_stereo)

        tv_on_cmd = TVOnCommand(living_room_tv)
        tv_off_cmd = TVOffCommand(living_room_tv)

        hottub_on_cmd = HottubOnCommand(hottub)
        hottub_off_cmd = HottubOffCommand(hottub)

        ''' Initialize Macro commands  '''
        party_mode_on = MacroCommand(
            [living_room_light_on_cmd, stereo_on_with_cd_cmd, tv_on_cmd, hottub_on_cmd])
        party_mode_off = MacroCommand(
            [living_room_light_off_cmd, stereo_off_cmd, tv_off_cmd, hottub_off_cmd])

        ''' Assign commands to slots '''
        self.remote.set_command(0, party_mode_on, party_mode_off)

        ''' Print remote '''
        print(self.remote)

    def test_on_button_was_pressed(self):
        """ Test the On buttons """

        self.remote.on_button_was_pressed(0)

        self.assertTrue(True)

    def test_off_button_was_pressed(self):
        """ Test the Off buttons """

        self.remote.off_button_was_pressed(0)

        self.assertTrue(True)

    def test_slot_0(self):
        """ Test slot 0 """
        self.remote.on_button_was_pressed(0)
        self.remote.off_button_was_pressed(0)




