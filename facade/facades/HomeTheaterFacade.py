from facade.devices.Amplifier import Amplifier
from facade.devices.Tuner import Tuner
from facade.devices.StreamingPlayer import StreamingPlayer
from facade.devices.Projector import Projector
from facade.devices.TheaterLights import TheaterLights
from facade.devices.Screen import Screen
from facade.devices.PopcornPopper import PopcornPopper


class HomeTheaterFacade:
    """ Implements a Facade """

    def __init__(self, amp: Amplifier, tuner: Tuner, player: StreamingPlayer, projector: Projector, lights: TheaterLights,
                 screen: Screen, popper: PopcornPopper):
        """ Initialize HomeTheaterFacade with all required devices """

        self.amp = amp
        self.tuner = tuner
        self.player = player
        self.projector = projector
        self.lights = lights
        self.screen = screen
        self.popper = popper

    def watch_movie(self, movie: str):
        """ Watch a movie """
        print('We are watching ', movie)
        self.popper.on()
        self.popper.pop()
        self.lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.wide_screen_mode()
        self.amp.on()
        self.amp.set_streaming_player(self.player)
        self.amp.set_stereo_sound()
        self.amp.set_volume(50)
        self.player.on()
        self.player.play(movie)

    def end_movie(self):
        print('Shutting down the movie theater...')
        self.popper.off()
        self.lights.off()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.player.stop()
        self.player.off()
