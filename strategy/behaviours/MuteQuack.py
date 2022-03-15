from strategy.behaviours.QuackBehaviour import QuackBehaviour


class MuteQuack(QuackBehaviour):

    def quack(self):
        print('...')
