from unittest import TestCase
from proxy.GumballMonitor import GumballMonitor


class TestGumballMonitor(TestCase):

    def setUp(self) -> None:
        self.monitor = GumballMonitor()

    def test_report(self):
        self.monitor.report()
