from unittest import TestCase
from template_method.sort.Duck import Duck


class TestDuck(TestCase):

    def setUp(self) -> None:
        self.ducks = [Duck("Daffy", 8),
                      Duck("Dewey", 2),
                      Duck("Howard", 7),
                      Duck("Louie", 2),
                      Duck("Donald", 10),
                      Duck("Huey", 2)
                      ]

    def test_duck_sorting(self):
        self.ducks.sort()
        for duck in self.ducks:
            print(duck)
