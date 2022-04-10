from unittest import TestCase
from proxy.GumballMonitor import GumballMonitor


class TestGumballMonitor(TestCase):

    def setUp(self) -> None:
        self.monitor_linz = GumballMonitor("GumballMachineLinz")
        self.monitor_salzburg = GumballMonitor("GumballMachineSalzburg")
        self.monitor_vienna = GumballMonitor("GumballMachineVienna")

    def test_report_linz(self):
        self.monitor_linz.report()

    def test_report_salzburg(self):
        self.monitor_salzburg.report()

    def test_report_vienna(self):
        self.monitor_vienna.report()
