from state.states.State import State
from state.states.NoQuarterState import NoQuarterState
from state.states.SoldOutState import SoldOutState
from state.states.HasQuarterState import HasQuarterState
from state.states.SoldState import SoldState
from state.states.WinnerState import WinnerState


class GumballMachine:
    """
    Gumball machine is the 'Context' in the context of State Pattern, no pun intended.
    """

    def __init__(self, count: int = 0):
        """
        Initialize the machine with states, and the number of gumballs
        """
        self.count = count

        self.sold_out_state = SoldOutState(self)
        self.no_quarter_state = NoQuarterState(self)
        self.has_quarter_state = HasQuarterState(self)
        self.sold_state = SoldState(self)
        self.winner_state = WinnerState(self)

        if self.count > 0:
            self.state = self.no_quarter_state
        else:
            self.state = self.sold_out_state

    def get_sold_out_state(self) -> State:
        """ Get SoldOut State address """
        return self.sold_out_state

    def get_no_quarter_state(self) -> State:
        """ Get NoQuarter State address """
        return self.no_quarter_state

    def get_has_quarter_state(self) -> State:
        """ Get HasQuarter State address """
        return self.has_quarter_state

    def get_sold_state(self) -> State:
        """ Get Sold State address """
        return self.sold_state

    def get_winner_state(self) -> State:
        """ Get Winner State address """
        return self.winner_state

    def insert_quarter(self):
        """ Insert quarter request """
        self.state.insert_quarter()

    def eject_quarter(self):
        """ Eject quarter request """
        self.state.eject_quarter()

    def turn_crank(self):
        """ Turn crank request """
        self.state.turn_crank()
        self.state.dispense()

    def refill(self, count):
        """ Refill request """
        self.count = count
        print('The gumball machine was just refilled!')
        self.state.refill()

    def set_state(self, state: State):
        """ Set state """
        self.state = state

    def get_count(self) -> int:
        """ Get gumball count """
        return self.count

    def dec_count(self):
        """ Decrement gumball count """
        self.count -= 1

    def __str__(self):
        company_desc = 'Mighty Gumball, Inc.\n'
        machine_desc = 'Python-enabled Standing Gumball 2000, model #2022\n'
        count_desc = 'Number of gumballs: {:d}\n'.format(self.get_count())

        state_desc = ''
        if self.state == self.no_quarter_state:
            state_desc = 'Machine is waiting for a quarter'
        elif self.state == self.has_quarter_state:
            state_desc = 'The machine has a quarter'
        elif self.state == self.sold_state:
            state_desc = 'The machine is in the sold state. It wil dispense if there are gumballs in the machine'
        elif self.state == self.sold_out_state:
            state_desc = 'The machine is out of gumballs'

        return '\n' + company_desc + machine_desc + count_desc + state_desc + '\n'
