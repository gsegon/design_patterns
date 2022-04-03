import Pyro4
from proxy.rmi_example.MyRemote import MyRemote


class MyRemoteClient:
    """
    Client that 1st retrieves the 'stub' or Proxy from the nameserver and then calls the method specified in
    MyRemote on the retrieved object
    """

    def get_proxy(self) -> MyRemote:
        """ Get the Proxy (aka. stub or service) from the nameserver.  """
        service = Pyro4.Proxy("PYRONAME:RemoteHello")
        return service

    def go(self):
        """ Call the methods on the remote object. The remote object implements MyRemote so we call methods that are
        specified in MyRemote. """
        service = self.get_proxy()
        print(service.say_hello())
