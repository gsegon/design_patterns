import unittest
from adapter.turkeys.Turkey import Turkey
from adapter.ducks.MallardDuck import MallardDuck
from adapter.turkeys.WildTurkey import WildTurkey
from adapter.adapters.DuckAdapter import DuckAdapter


def test_turkey(turkey: Turkey):
    """ Represents client code using Duck interface """
    turkey.fly()
    turkey.gobble()


class TestDuckTestDrive(unittest.TestCase):
    """ Basic Duck testing """

    # TODO: Make 'multi-dataset' testing
    def setUp(self) -> None:
        """ Setup sort to test """
        self.wild_turkey = WildTurkey()
        mallard_duck = MallardDuck()
        self.duck_adapter = DuckAdapter(mallard_duck)

    def test_wild_turkey(self):
        """ tests wild turkey """
        test_turkey(self.wild_turkey)

    def test_duck_adapter(self):
        """ Tests duck_adapter """
        test_turkey(self.duck_adapter)
