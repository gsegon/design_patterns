import Pyro4


class MyRemoteClient:

    def go(self):
        service = Pyro4.Proxy("PYRONAME:RemoteHello")
        print(service.say_hello())
