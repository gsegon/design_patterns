from facade.devices.StreamingPlayer import StreamingPlayer
from facade.devices.Tuner import Tuner


class Amplifier:
    """ Amplifier device class """

    def __init__(self):
        self.streaming_player = None
        self.tuner = None

        self.volume = 20  # 0-100

    def on(self):
        """ Turn the amplifier on """
        print("Amplifier is ON")

    def off(self):
        """ Turn the amplifier off """
        print("Amplifier is OFF")

    def set_streaming_player(self, streaming_player: StreamingPlayer):
        """ Sets the streaming player """
        self.streaming_player = streaming_player
        print("Set the streaming player")

    def set_stereo_sound(self):
        """ set stereo sound """
        print('Stereo sound is set')

    def set_tuner(self, tuner: Tuner):
        """ Set the tuner """
        self.tuner = tuner

    def set_volume(self, volume: int):
        """ Set the volume """
        self.volume = volume

