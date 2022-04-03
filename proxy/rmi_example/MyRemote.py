import Pyro4
from abc import ABC, abstractmethod


@Pyro4.expose
class MyRemote(ABC):
    """ The Remote interface """

    @abstractmethod
    def say_hello(self) -> str:
        """ Remote method """
        pass
