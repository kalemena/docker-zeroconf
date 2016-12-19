#!/usr/bin/env python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

import logging
import socket
import sys
from time import sleep
import SocketServer
from zeroconf import *
# from zeroconf import ServiceBrowser, ServiceStateChange, Zeroconf
import socket
import time
 
PORT = 7679
devices = [];

class ServiceListener(object):
    def __init__(self):
        self.r = Zeroconf()
 
    def remove_service(self, zeroconf, type, name):
        print()
        print("Service %s removed" % (name))
 
    def add_service(self, zeroconf, type, name):
        print()
        print("Service %s added" % (name))
        print("  Type is %s" % (type))
        info = self.r.get_service_info(type, name)
        if info:
            #Currently only saving the ip address.
            devices.append(socket.inet_ntoa(info.address))
            print("  Address is %s:%d" % (socket.inet_ntoa(info.address), info.port))
            print("  Weight is %d, Priority is %d" % (info.weight, info.priority))
            print("  Server is %s" % (info.server))
            prop = info.properties
            if prop:
                print("  Properties are")
                for key, value in prop.items():
                    print("    %s: %s" % (key, value))
            else:
                print("  No properties")
        else:
            print("  No info")
        print('\n')
         
def searchForDynamixServices():
    del devices[:] # Clear list.
    zeroconf = Zeroconf()
    listener = ServiceListener()
    browser = ServiceBrowser(zeroconf, "_dynamix._tcp.local.", listener)
    #Will only be searching for 5 seconds. 
    time.sleep(5)
    zeroconf.close()
    return devices[0]
 
# This class hosts a Simple HTTP Server at 127.0.0.1:7679.
# To search for devices, http://127.0.0.1:7679/search
 
class CustomHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path=='/search':
            #This URL will trigger our sample function and send what it returns back to the browser
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            # write the list of ip address as a response.
            self.wfile.write(searchForDynamixServices())
            return
        else:
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            # Send the html message
            self.wfile.write("Nothing here !")
            return
 
try:
  server = HTTPServer(('', PORT), CustomHandler)
  print("Started httpserver on port %s" % (PORT))
  server.serve_forever()

except KeyboardInterrupt:
  print("^C received, shutting down the web server")
  server.socket.close()
