from abc import ABC, abstractmethod


class State(ABC):
    """ Interface for all states """

    @abstractmethod
    def insert_quarter(self):
        """ Insert quarter transition """
        pass

    @abstractmethod
    def eject_quarter(self):
        """ Eject quarter transition """
        pass

    @abstractmethod
    def turn_crank(self):
        """ Turn crank transition """
        pass

    @abstractmethod
    def dispense(self):
        """ Dispense transition """
        pass

    @abstractmethod
    def refill(self):
        """ Refill transition """
        pass
