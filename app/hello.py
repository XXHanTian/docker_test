# coding: utf-8

import socket
import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

ip = get_ip_address('eth0')

def app(env, start_response):
    if env.get("QUERY_STRING"):
        s = env.get("QUERY_STRING")
        i = s.split('=')[1]
        i = int(i)
    else:
        i = 1000
    res = 1
    for x in range(i):
        res = res * x
        
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World: {} and {}".format(ip, res)]
