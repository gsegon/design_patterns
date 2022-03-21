from factory.abstract_factory.ingredients.PizzaIngredientFactory import PizzaIngredientFactory

''' Imports abstracts for type hinting and implementations '''
from typing import List
from factory.abstract_factory.ingredients.clams.Clams import Clams
from factory.abstract_factory.ingredients.cheeses.Cheese import Cheese
from factory.abstract_factory.ingredients.sauces.Sauce import Sauce
from factory.abstract_factory.ingredients.pepperoni.Pepperoni import Pepperoni
from factory.abstract_factory.ingredients.doughs.Dough import Dough
from factory.abstract_factory.ingredients.veggies.Veggie import Veggie

from factory.abstract_factory.ingredients.doughs.ThinCrustDough import ThinCrustDough
from factory.abstract_factory.ingredients.clams.FreshClams import FreshClams
from factory.abstract_factory.ingredients.cheeses.ReggianoCheese import ReggianoCheese
from factory.abstract_factory.ingredients.sauces.MarinaraSauce import MarinaraSauce
from factory.abstract_factory.ingredients.pepperoni.SlicedPepperoni import SlicedPepperoni
from factory.abstract_factory.ingredients.veggies.OnionVeggie import OnionVeggie
from factory.abstract_factory.ingredients.veggies.GarlicVeggie import GarlicVeggie
from factory.abstract_factory.ingredients.veggies.MushroomVeggie import MushroomVeggie
from factory.abstract_factory.ingredients.veggies.RedPepperVeggie import RedPepperVeggie


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    """ This is a concrete factory implementing the abstract factory """

    def create_dough(self) -> Dough:
        return ThinCrustDough()

    def create_cheese(self) -> Cheese:
        return ReggianoCheese()

    def create_clams(self) -> Clams:
        return FreshClams()

    def create_sauce(self) -> Sauce:
        return MarinaraSauce()

    def create_veggies(self) -> List[Veggie]:
        return [OnionVeggie(), GarlicVeggie(), MushroomVeggie(), RedPepperVeggie()]

    def create_pepperoni(self) -> Pepperoni:
        return SlicedPepperoni()
