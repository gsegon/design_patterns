from Duck import Duck


class MallardDuck(Duck):

    def __init__(self):
        self._flying_capacity = 100

    def get_flying_capacity(self) -> int:
        return self._flying_capacity

    def quack(self):
        print('Quack!')

    def fly(self):
        print('I\'m flying! With ', self.get_flying_capacity(), 'flying capacity!')