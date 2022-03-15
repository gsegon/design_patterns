from strategy.clients.Duck import Duck
from strategy.behaviours.MuteQuack import MuteQuack
from strategy.behaviours.FlyNoWay import FlyNoWay


class DecoyDuck(Duck):

    def __init__(self):
        self._fly_behaviour = FlyNoWay()
        self._quack_behaviour = MuteQuack()

    def display(self):
        print('*shows a picture of Decoy duck*')

