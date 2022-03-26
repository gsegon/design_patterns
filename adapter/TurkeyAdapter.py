from Duck import Duck
from Turkey import Turkey


class TurkeyAdapter(Duck):

    def __init__(self, turkey: Turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for _ in range(5):
            self.turkey.fly()

