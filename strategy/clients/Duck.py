from abc import ABC, abstractmethod, abstractproperty


class Duck(ABC):

    @abstractmethod
    def __init__(self):
        self._fly_behaviour = None
        self._quack_behaviour = None

    @property
    def fly_behaviour(self):
        return self._fly_behaviour

    def set_fly_behaviour(self, val):
        self._fly_behaviour = val

    @property
    def quack_behaviour(self):
        return self._quack_behaviour

    def set_quack_behaviour(self, val):
        self._quack_behaviour = val

    def swim(self):
        print(__class__.__name__, ' is swimming...')
        pass

    def perform_quack(self):
        self.quack_behaviour.quack()

    def perform_fly(self):
        self.fly_behaviour.fly()

    @abstractmethod
    def display(self):
        pass
