from facade.devices.StreamingPlayer import StreamingPlayer


class Projector:
    """ Projector device class """

    def __init__(self, player: StreamingPlayer):
        self.player = player

    def on(self):
        """ Turn the projector on """
        print("Projector is ON")

    def off(self):
        """ Turn the projector off """
        print('Projector is OFF')

    def tv_mode(self):
        """ Set projector to TV mode """
        print('Projector in TV mode')

    def wide_screen_mode(self):
        """ Set projector to wide screen mode """
        print('Projector in wide screen mode')
