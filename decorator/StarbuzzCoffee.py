from Espresso import Espresso
from DarkRoast import DarkRoast
from HouseBlend import HouseBlend

from Mocha import Mocha
from Soy import Soy
from Whip import Whip

if __name__ == '__main__':

    beverage = Espresso()
    print(beverage.get_description(), ' $', beverage.cost())

    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(beverage2.get_description(), ' $', beverage2.cost())

    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(beverage3.get_description(), ' $', beverage3.cost())

    beverage4 = HouseBlend()
    beverage4.set_size('GRANDE')
    beverage4 = Soy(beverage4)
    beverage4 = Mocha(beverage4)
    beverage4 = Whip(beverage4)
    print(beverage4.get_description(), ' $', beverage4.cost())
