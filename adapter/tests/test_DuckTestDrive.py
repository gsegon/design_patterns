import unittest
from adapter.ducks.Duck import Duck
from adapter.ducks.MallardDuck import MallardDuck
from adapter.turkeys.WildTurkey import WildTurkey
from adapter.adapters.TurkeyAdapter import TurkeyAdapter


def test_duck(duck: Duck):
    """ Represents client code using Duck interface """
    duck.fly()
    duck.quack()


class TestDuckTestDrive(unittest.TestCase):
    """ Basic Duck testing """

    # TODO: Make 'multi-dataset' testing
    def setUp(self) -> None:
        """ Setup sort to test """
        self.mallard_duck = MallardDuck()
        turkey = WildTurkey()
        self.turkey_adapter = TurkeyAdapter(turkey)

    def test_mallard_duck(self):
        """ tests mallard duck """
        test_duck(self.mallard_duck)

    def test_turkey_adapter(self):
        """ tests turkey_adapter """
        test_duck(self.turkey_adapter)
