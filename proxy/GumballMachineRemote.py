from abc import ABC, abstractmethod
from state.states.State import State


class GumballMachineRemote(ABC):
    """ The Remote interface """

    @abstractmethod
    def get_location(self) -> str:
        """ Get location """
        raise Exception

    @abstractmethod
    def get_count(self) -> int:
        """ Get count """
        raise Exception

    @abstractmethod
    def get_state(self) -> State:
        """ Get state """
        raise Exception
