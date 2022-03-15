from strategy.clients.Duck import Duck
from strategy.behaviours.Squeak import Squeak
from strategy.behaviours.FlyNoWay import FlyNoWay


class RubberDuck(Duck):

    def __init__(self):
        self._fly_behaviour = FlyNoWay()
        self._quack_behaviour = Squeak()

    def display(self):
        print('*shows a picture of Rubber duck*')

