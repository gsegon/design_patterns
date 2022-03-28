

class Duck:

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __str__(self):
        return '{:} : {:2f}'.format(self.name, self.weight)

