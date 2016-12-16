
# docker-zeroconf

This images demonstrate minimal ZeroConf using python-zeroconf library.

Two containers are created with one listening and the other looping on register/unregister.

The python samples running in images are copied from [python zeroconf github pages](https://github.com/paulsm/pyzeroconf).


# How-To

## Build

```bash
$ docker-compose build
```

## Run

```bash
$ docker-compose up
```

# Sample output

```bash
$ docker-compose logs -f
Attaching to pythonzeroconf_registrator_1, pythonzeroconf_browser_1
registrator_1  | Registration of a service, press Ctrl-C to exit...
registrator_1  | Registering...
browser_1      | 
browser_1      | Browsing services, press Ctrl-C to exit...
browser_1      | 
browser_1      | Service Paul's Test Web Site._http._tcp.local. of type _http._tcp.local. state changed: ServiceStateChange.Added
browser_1      |   Address: 127.0.0.1:80
browser_1      |   Weight: 0, priority: 0
browser_1      |   Server: ash-2.local.
browser_1      |   Properties are:
browser_1      |     path: /~paulsm/
browser_1      | 
browser_1      | 
registrator_1  | Unregistering...
browser_1      | Service Paul's Test Web Site._http._tcp.local. of type _http._tcp.local. state changed: ServiceStateChange.Removed
registrator_1  | Registering...
browser_1      | Service Paul's Test Web Site._http._tcp.local. of type _http._tcp.local. state changed: ServiceStateChange.Added
browser_1      |   Address: 127.0.0.1:80
browser_1      |   Weight: 0, priority: 0
browser_1      |   Server: ash-2.local.
browser_1      |   Properties are:
browser_1      |     path: /~paulsm/
browser_1      | 
browser_1      | 
registrator_1  | Unregistering...
browser_1      | Service Paul's Test Web Site._http._tcp.local. of type _http._tcp.local. state changed: ServiceStateChange.Removed
registrator_1  | Registering...
browser_1      | Service Paul's Test Web Site._http._tcp.local. of type _http._tcp.local. state changed: ServiceStateChange.Added
browser_1      |   Address: 127.0.0.1:80
browser_1      |   Weight: 0, priority: 0
browser_1      |   Server: ash-2.local.
browser_1      |   Properties are:
browser_1      |     path: /~paulsm/
```

# References

https://pypi.python.org/pypi/zeroconf

http://stackoverflow.com/questions/1916017/simplest-way-to-publish-over-zeroconf-bonjour

https://vshivam.wordpress.com/2015/02/17/multicast-dns-service-discovery-in-python/

