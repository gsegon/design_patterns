from abc import ABC, abstractmethod

from typing import List
from factory.abstract_factory.ingredients.cheeses.Cheese import Cheese
from factory.abstract_factory.ingredients.sauces.Sauce import Sauce
from factory.abstract_factory.ingredients.clams.Clams import Clams
from factory.abstract_factory.ingredients.doughs.Dough import Dough
from factory.abstract_factory.ingredients.veggies.Veggie import Veggie
from factory.abstract_factory.ingredients.pepperoni import Pepperoni


class PizzaIngredientFactory(ABC):
    """ This is an abstract factory """

    @abstractmethod
    def create_dough(self) -> Dough:
        pass

    @abstractmethod
    def create_clams(self) -> Clams:
        pass

    @abstractmethod
    def create_sauce(self) -> Sauce:
        pass

    @abstractmethod
    def create_cheese(self) -> Cheese:
        pass

    @abstractmethod
    def create_veggies(self) -> List[Veggie]:
        pass

    @abstractmethod
    def create_pepperoni(self) -> Pepperoni:
        pass
