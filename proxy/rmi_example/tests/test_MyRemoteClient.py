from unittest import TestCase
from proxy.rmi_example.MyRemoteClient import MyRemoteClient


class TestMyRemoteClient(TestCase):
    """
    Instantiate a Remote Client object and call the method go which
    1st: Receives the 'service' proxy. In our case the 'service' is 'RemoteHello' (MyRemoteImpl is registered to the
     nameserver as 'RemoteHello')
    """

    def setUp(self) -> None:
        self.my_remote_client = MyRemoteClient()

    def test_go(self):
        self.my_remote_client.go()
