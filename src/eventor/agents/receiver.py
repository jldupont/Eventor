'''
Created on 2011-03-18

@author: jldupont
'''
from eventor.system.base import AgentThreadedBase
from eventor.system.network import MulticastReceiver

class Receiver(AgentThreadedBase):
    
    GROUP = "239.0.0.1"
    PORT  = 6666
    COUNT = 10
    
    def __init__(self):
        AgentThreadedBase.__init__(self)
        
        self.mr=MulticastReceiver(self.GROUP, self.PORT)
        
    def loop(self):
        count=self.COUNT
        
        data=self.mr.get()
        while data and count>0:
            self.pub("mmsg", data)
            data=self.mr.get()
            count=count-1


_=Receiver()
_.start()

        