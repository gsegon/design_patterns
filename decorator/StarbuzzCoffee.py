from decorator.beverages.Espresso import Espresso
from decorator.beverages.DarkRoast import DarkRoast
from decorator.beverages.HouseBlend import HouseBlend

from decorator.condiments.Mocha import Mocha
from decorator.condiments.Soy import Soy
from decorator.condiments.Whip import Whip

if __name__ == '__main__':

    ''' Instantiate an Espresso '''
    beverage = Espresso()
    print(beverage.get_description(), ' $', beverage.cost())

    ''' Instantiate a Dark Roast '''
    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(beverage2.get_description(), ' $', beverage2.cost())

    ''' Instantiate a House Blend '''
    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(beverage3.get_description(), ' $', beverage3.cost())

    ''' Instantiate a Grande House Blend '''
    beverage4 = HouseBlend()
    beverage4.set_size('GRANDE')
    beverage4 = Soy(beverage4)
    beverage4 = Mocha(beverage4)
    beverage4 = Whip(beverage4)
    print(beverage4.get_description(), ' $', beverage4.cost())
