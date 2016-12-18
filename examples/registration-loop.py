#!/usr/bin/env python

""" Example of announcing a service (in this case, a fake HTTP server) """

import logging
import socket
import sys
from time import sleep

from zeroconf import ServiceInfo, Zeroconf

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))
    if len(sys.argv) > 1:
        assert sys.argv[1:] == ['--debug']
        logging.getLogger('zeroconf').setLevel(logging.DEBUG)

    hostname = socket.gethostname()
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('google.com', 0))
    hostip = s.getsockname()[0]
    
    print("hostname = " + hostname)
    print("ip = " + hostip)
    
    desc = {'name': hostname}
    info = ServiceInfo("_http._tcp.local.",
                       hostname + " Test Web Site._http._tcp.local.",
                       socket.inet_aton(hostip), 80, 0, 0,
                       desc, hostname + ".local.")

    zeroconf = Zeroconf()
    print("Registration of a service, press Ctrl-C to exit...")
    
    try:
        while True:
	    print("Registering " + hostname + "...")
	    zeroconf.register_service(info)
            sleep(20)
            print("Unregistering " + hostname + "...")
            zeroconf.unregister_service(info)
            sleep(20)
    except KeyboardInterrupt:
        pass
    finally:        
        zeroconf.close()
