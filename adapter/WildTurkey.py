from Turkey import Turkey


class WildTurkey(Turkey):

    def __init__(self):
        self._flying_capacity = 20

    def get_flying_capacity(self) -> float:
        return self._flying_capacity

    def gobble(self):
        print('Gobble gobble')

    def fly(self):
        print('I\'m flying a short distance')
        