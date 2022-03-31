from state.states.State import State


class NoQuarterState(State):
    """ Implements the NoQuarter State """

    def __init__(self, gumball_machine: 'GumballMachine'):
        """ Initialize """
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        """ Insert quarter transition """
        print('You inserted a quarter')
        self.gumball_machine.set_state(self.gumball_machine.get_has_quarter_state())

    def eject_quarter(self):
        """ Eject quarter transition """
        print('You haven\'t inserted a quarter')

    def turn_crank(self):
        """ Turn crank transition """
        print('You turned but there is no quarter')

    def dispense(self):
        """ Dispense transition """
        print('You need to pay first')

    def refill(self):
        """ Refill transition """
        pass
