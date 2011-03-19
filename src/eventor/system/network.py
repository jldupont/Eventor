'''
Created on 2011-03-18

@author: jldupont
'''
import socket
import struct
import select


class MulticastReceiver(object):
    
    def __init__(self, group, port):
        self.port=port
        self.group=group
        
        self.socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(('', port))
        
        mreq = struct.pack("4sl", socket.inet_aton(group), socket.INADDR_ANY)
        self.socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        
    def get(self, timeout=2.0):

        iready, _oready, _eready = select.select([self.socket], [], [], timeout)
        
        data=None
        for s in iready:
            data=s.recv(8192)
            
        return data
