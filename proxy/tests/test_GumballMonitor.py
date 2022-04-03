from unittest import TestCase
from proxy.GumballMachine import GumballMachine
from proxy.GumballMonitor import GumballMonitor


class TestGumballMonitor(TestCase):

    def setUp(self) -> None:
        self.machine = GumballMachine("Linz 4020", 16)
        self.monitor = GumballMonitor(self.machine)

    def test_report(self):
        self.monitor.report()
