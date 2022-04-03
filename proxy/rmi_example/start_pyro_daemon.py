import Pyro4
from MyRemoteImpl import MyRemoteImpl

if __name__ == '__main__':
    """
    Equivalent of running rmiregistry command as shown in the Java example
    
    Make sure that the Pyro nameserver is running. You can start one by typing the following command: 
    python -m Pyro4.naming (or simply: pyro4-ns) in a separate console window (usually there is just one name server 
    running in your network).
    """
    daemon = Pyro4.Daemon()             # Make a Pyro daemon
    ns = Pyro4.locateNS()               # Find the name server
    uri = daemon.register(MyRemoteImpl, objectId='1')   # Register the class. It is only known to the daemon, not to
                                                        # nameserver also. Returns the uri of the registered object.
    ns.register('RemoteHello', uri)     # Register the object with a nme in the name server.
    daemon.requestLoop()                # Start the event loop of the server to wait for calls