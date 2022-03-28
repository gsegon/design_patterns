from unittest import TestCase
from template_method.Tea import Tea


class TestTea(TestCase):

    def setUp(self) -> None:
        self.tea = Tea()

    def test_prepare_recipe(self):
        self.tea.prepare_recipe()
