from abc import ABC, abstractmethod


class Command(ABC):
    """ Command abstract """

    @abstractmethod
    def execute(self):
        """ Execute the command """
        pass

    @abstractmethod
    def undo(self):
        """ Undo the command """
        pass
