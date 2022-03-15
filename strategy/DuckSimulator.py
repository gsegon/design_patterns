from clients.RubberDuck import RubberDuck
from clients.MallardDuck import MallardDuck
from clients.DecoyDuck import DecoyDuck
from clients.RedheadDuck import RedheadDuck

from behaviours.FlyNoWay import FlyNoWay
from behaviours.FlyRocket import FlyRocket

if __name__ == '__main__':

    print('Meet rubby...a RubberDuck:')
    rubby = RubberDuck()
    rubby.perform_quack()
    rubby.display()
    rubby.perform_fly()

    print('\nMeet mallard...a MallardDuck:')
    mallard = MallardDuck()
    mallard.perform_quack()
    mallard.display()
    mallard.perform_fly()

    print('\nMeet Deck...a DecoyDuck:')
    deck = DecoyDuck()
    deck.perform_quack()
    deck.display()
    deck.perform_fly()

    print('\nMeet Red...a RedheadDuck:')
    red = RedheadDuck()
    red.perform_quack()
    red.display()
    red.perform_fly()

    red.set_fly_behaviour(FlyNoWay())   # Poor red breaks a wings and can't fly!
    red.perform_fly()

    red.set_fly_behaviour(FlyRocket())   # Luckly, finds a rocket...
    red.perform_fly()


