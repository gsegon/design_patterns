import Pyro4
from proxy.rmi_example.MyRemote import MyRemote


@Pyro4.expose
class MyRemoteImpl(MyRemote):
    """ Remote implementation """

    def say_hello(self) -> str:
        """ Implementation of the specified remote method """
        return "Server says 'Hey'"
