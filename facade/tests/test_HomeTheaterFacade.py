import unittest

from facade.devices.Amplifier import Amplifier
from facade.devices.Tuner import Tuner
from facade.devices.StreamingPlayer import StreamingPlayer
from facade.devices.Projector import Projector
from facade.devices.TheaterLights import TheaterLights
from facade.devices.Screen import Screen
from facade.devices.PopcornPopper import PopcornPopper

from facade.facades.HomeTheaterFacade import HomeTheaterFacade


class TestHomeTheaterFacade(unittest.TestCase):

    def setUp(self) -> None:
        amp = Amplifier()
        tuner = Tuner(amp)
        player = StreamingPlayer(amp)

        amp.set_streaming_player(player)
        amp.set_tuner(tuner)

        projector = Projector(player)
        lights = TheaterLights()
        screen = Screen()
        popper = PopcornPopper()

        self.home_theater = HomeTheaterFacade(amp, tuner, player, projector, lights, screen, popper)

    def test_watch_movie(self):
        self.home_theater.watch_movie('Batman: The Dark Knight')

    def test_end_movie(self):
        self.home_theater.end_movie()


