from state.states.State import State
import random
from datetime import datetime


class HasQuarterState(State):
    """ Implements the SoldOut State """

    def __init__(self, gumball_machine: 'GumballMachine'):
        """ Initialize """
        self.gumball_machine = gumball_machine
        random.seed(datetime.now())

    def insert_quarter(self):
        """ Insert quarter transition """
        print('You can\'t insert another quarter')

    def eject_quarter(self):
        """ Eject quarter transition """
        self.gumball_machine.set_state(self.gumball_machine.get_no_quarter_state())
        print('Quarter returned')

    def turn_crank(self):
        """ Turn crank transition """
        print('You turned...')
        winner = random.randint(0, 10)
        if winner == 0:
            self.gumball_machine.set_state(self.gumball_machine.get_winner_state())
        else:
            self.gumball_machine.set_state(self.gumball_machine.get_sold_state())

    def dispense(self):
        """ Dispense transition """
        print('You need to turn the crank')

    def refill(self):
        """ Refill transition """
        pass
