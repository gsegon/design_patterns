from unittest import TestCase
from command.SimpleRemoteControl import SimpleRemoteControl

from command.vendors.Light import Light
from command.commands.LightOnCommand import LightOnCommand

from command.vendors.GarageDoor import GarageDoor
from command.commands.GarageDoorOpenCommand import GarageDoorOpen


class TestSimpleRemoteControl(TestCase):

    def setUp(self) -> None:
        """ Setup the remote """
        self.remote = SimpleRemoteControl()

    def test_button_was_pressed(self):
        """ Test button pressing """

        ''' Instantiate the vendor Light() and construct a light_on_cmd command '''
        light = Light('Living room')
        light_on_cmd = LightOnCommand(light)

        ''' Instantiate the vendor GarageDoor() and construct a garage_door_open_cmd command'''
        garage_door = GarageDoor()
        garage_door_open_cmd = GarageDoorOpen(garage_door)

        ''' Set the command of the invoker to light_on_cmd and simulate button press '''
        self.remote.set_command(light_on_cmd)
        self.remote.button_was_pressed()

        ''' Set the command of the invoker to garage_door_open_cmd and simulate button press '''
        self.remote.set_command(garage_door_open_cmd)
        self.remote.button_was_pressed()

        self.assertTrue(True)
