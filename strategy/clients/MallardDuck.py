from strategy.clients.Duck import Duck
from strategy.behaviours.Quack import Quack
from strategy.behaviours.FlyWithWings import FlyWithWings


class MallardDuck(Duck):

    def __init__(self):
        self._fly_behaviour = FlyWithWings()
        self._quack_behaviour = Quack()

    def display(self):
        print('*shows a picture of Mallard duck*')

