import unittest
from Duck import Duck
from MallardDuck import MallardDuck
from WildTurkey import WildTurkey
from TurkeyAdapter import TurkeyAdapter


def test_duck(duck: Duck):
    """ Represents client code using Duck interface """
    duck.fly()
    duck.quack()


class TestDuckTestDrive(unittest.TestCase):
    """ Basic Duck testing """

    # TODO: Make 'multi-dataset' testing
    def setUp(self) -> None:
        """ Setup ducks to test """
        self.mallard_duck = MallardDuck()
        turkey = WildTurkey()
        self.turkey_adapter = TurkeyAdapter(turkey)

    def test_mallard_duck(self):
        """ tests mallard duck """
        test_duck(self.mallard_duck)

    def test_turkey_adapter(self):
        """ tests turkey_adapter """
        test_duck(self.turkey_adapter)
