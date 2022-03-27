# from facade.devices.Amplifier import Amplifier


class StreamingPlayer:
    """ StreamingPlayer device class """

    def __init__(self, amplifier):
        self.amplifier = amplifier

    def on(self):
        """ Turn the Streaming Player on """
        print("Streaming player is ON")

    def off(self):
        """ Turn the Streaming Player off """
        print('Streaming player is OFF')

    def pause(self):
        """ Pause the streaming player """
        print('Streaming player is PAUSED')

    def play(self, movie: str):
        """ Play the streaming player """
        print('Streaming player is PLAYING: ', movie)

    def set_surround_audio(self):
        """ Set surround audio """
        print('Set surround audio')

    def set_two_channel_audio(self):
        """ Set two channel audio """
        print('Two channel audio set')

    def stop(self):
        """ Stop streaming player """
        print('Streaming player STOPPED')
