from state.states.State import State


class SoldOutState(State):
    """ Implements the SoldOut State """

    def __init__(self, gumball_machine: 'GumballMachine'):
        """ Initialize """
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        """ Insert quarter transition """
        print('You can\'t insert a quarter, the machine is sold out')

    def eject_quarter(self):
        """ Eject quarter transition """
        print('You can\'t eject, you haven\'t inserted a quarter yet')

    def turn_crank(self):
        """ Turn crank transition """
        print('You turned but there are no gumballs')

    def dispense(self):
        """ Dispense transition """
        print('No gumball dispensed')

    def refill(self):
        """ Refill transition """
        self.gumball_machine.set_state(self.gumball_machine.get_no_quarter_state())
