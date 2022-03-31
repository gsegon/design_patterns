from unittest import TestCase
from state.GumballMachine import GumballMachine


class TestGumballMachine(TestCase):

    def setUp(self) -> None:
        self.gumball_machine = GumballMachine(5)

    def test_in_house(self):
        print(self.gumball_machine)

        self.gumball_machine.insert_quarter()
        self.gumball_machine.turn_crank()

        print(self.gumball_machine)

        self.gumball_machine.insert_quarter()
        self.gumball_machine.eject_quarter()
        self.gumball_machine.turn_crank()

        print(self.gumball_machine)

        self.gumball_machine.insert_quarter()
        self.gumball_machine.turn_crank()
        self.gumball_machine.insert_quarter()
        self.gumball_machine.turn_crank()
        self.gumball_machine.eject_quarter()

        print(self.gumball_machine)

        self.gumball_machine.insert_quarter()
        self.gumball_machine.insert_quarter()
        self.gumball_machine.turn_crank()
        self.gumball_machine.insert_quarter()
        self.gumball_machine.turn_crank()
        self.gumball_machine.insert_quarter()
        self.gumball_machine.turn_crank()

        print(self.gumball_machine)

    def test_winner(self):

        self.gumball_machine.count = 100

        for _ in range(100):
            self.gumball_machine.insert_quarter()
            self.gumball_machine.turn_crank()

    def test_refill(self):

        for _ in range(5):
            self.gumball_machine.insert_quarter()
            self.gumball_machine.turn_crank()

        self.gumball_machine.refill(5)
        self.gumball_machine.insert_quarter()
        self.gumball_machine.turn_crank()
