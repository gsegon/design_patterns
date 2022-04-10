import Pyro4
from proxy.GumballMachineRemote import GumballMachineRemote

''' Setting up the serializer '''
Pyro4.config.SERIALIZER = 'pickle'


class GumballMonitor:
    """
    Client that 1st retrieves the 'stub' or Proxy from the nameserver and then calls the method specified in
    MyRemote on the retrieved object
    """

    def __init__(self):
        self.machine = self.get_proxy()

    def get_proxy(self) -> GumballMachineRemote:
        """ Get the Proxy (aka. stub or service) from the nameserver.  """
        ns = Pyro4.locateNS()
        uri = ns.lookup("GumballMachine")
        return Pyro4.Proxy(uri)

    def report(self):
        print("Gumball Machine: ", self.machine.get_location())
        print("Current inventory: ", self.machine.get_count(), " gumballs")
        print("Current state: ", self.machine.get_state())
