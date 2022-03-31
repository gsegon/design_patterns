from state.states.State import State


class SoldState(State):
    """ Implements the Sold State """

    def __init__(self, gumball_machine: 'GumballMachine'):
        """ Initialize """
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        """ Insert quarter transition """
        print('Please wait, we\'re already giving you are gumball')

    def eject_quarter(self):
        """ Eject quarter transition """
        print('Sorry, you already turned the crank')

    def turn_crank(self):
        """ Turn crank transition """
        print('Turning twice doesn\'t get you another gumball')

    def dispense(self):
        """ Dispense transition """
        print('A gumball comes rolling out of the machine')

        self.gumball_machine.dec_count()
        if self.gumball_machine.get_count() == 0:
            print('Oops, out of gumballs!')
            self.gumball_machine.set_state(self.gumball_machine.get_sold_out_state())
        else:
            self.gumball_machine.set_state(self.gumball_machine.get_no_quarter_state())

    def refill(self):
        """ Refill transition """
        pass