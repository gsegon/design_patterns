from factory.abstract_factory.ingredients.PizzaIngredientFactory import PizzaIngredientFactory

''' Imports abstracts for type hinting and implementations '''
from typing import List
from factory.abstract_factory.ingredients.clams.Clams import Clams
from factory.abstract_factory.ingredients.cheeses.Cheese import Cheese
from factory.abstract_factory.ingredients.sauces.Sauce import Sauce
from factory.abstract_factory.ingredients.pepperoni.Pepperoni import Pepperoni
from factory.abstract_factory.ingredients.doughs.Dough import Dough
from factory.abstract_factory.ingredients.veggies.Veggie import Veggie

from factory.abstract_factory.ingredients.doughs.ThickCrustDough import ThickCrustDough
from factory.abstract_factory.ingredients.clams.FrozenClams import FrozenClams
from factory.abstract_factory.ingredients.cheeses.MozzarellaCheese import MozzarellaCheese
from factory.abstract_factory.ingredients.sauces.PlumTomatoSauce import PlumTomatoSauce
from factory.abstract_factory.ingredients.pepperoni.SlicedPepperoni import SlicedPepperoni
from factory.abstract_factory.ingredients.veggies.BlackOlivesVeggie import BlackOlivesVeggie
from factory.abstract_factory.ingredients.veggies.SpinachVeggie import SpinachVeggie
from factory.abstract_factory.ingredients.veggies.EggplantVeggie import EggplantVeggie


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):

    def create_dough(self) -> Dough:
        return ThickCrustDough()

    def create_cheese(self) -> Cheese:
        return MozzarellaCheese()

    def create_clams(self) -> Clams:
        return FrozenClams()

    def create_sauce(self) -> Sauce:
        return PlumTomatoSauce()

    def create_veggies(self) -> List[Veggie]:
        return [BlackOlivesVeggie(), SpinachVeggie(), EggplantVeggie()]

    def create_pepperoni(self) -> Pepperoni:
        return SlicedPepperoni()
