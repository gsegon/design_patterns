from strategy.behaviours.FlyBehaviour import FlyBehaviour


class FlyNoWay(FlyBehaviour):

    def fly(self):
        print('Can\'t fly...')
