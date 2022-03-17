from abc import ABC, abstractmethod


class Subject(ABC):

    @abstractmethod
    def register_observer(self, o):
        pass

    @abstractmethod
    def remove_observer(self, o):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

