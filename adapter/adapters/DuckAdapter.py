from adapter.turkeys.Turkey import Turkey
from adapter.ducks.Duck import Duck


class DuckAdapter(Turkey):

    def __init__(self, duck: Duck):
        self.duck = duck

    def get_flying_capacity(self) -> float:
        return self.duck.get_flying_capacity()/5

    def gobble(self):
        self.duck.quack()

    def fly(self):
        print('I\'m flying! With', self.get_flying_capacity(), ' flying capacity!' )