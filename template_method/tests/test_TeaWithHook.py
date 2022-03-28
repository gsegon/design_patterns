from unittest import TestCase
from template_method.TeaWithHook import TeaWithHook


class TestTeaWithHook(TestCase):

    def setUp(self) -> None:
        self.coffee = TeaWithHook()

    def test_prepare_recipe(self):
        self.coffee.prepare_recipe()