from Duck import Duck
from Turkey import Turkey


class TurkeyAdapter(Duck):

    def __init__(self, turkey: Turkey):
        self.turkey = turkey

    def get_flying_capacity(self) -> float:
        return self.turkey.get_flying_capacity()*5

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        print('I\'m flying! With', self.get_flying_capacity(), ' flying capacity!' )

