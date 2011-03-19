'''
Created on 2011-03-18

@author: jldupont
'''
import json

from eventor.system.base import AgentThreadedBase
from eventor.system.network import MulticastReceiver

class Receiver(AgentThreadedBase):
    
    GROUP = "239.0.0.1"
    PORT  = 6666
    
    def __init__(self):
        AgentThreadedBase.__init__(self)
        
        self.mr=MulticastReceiver(self.GROUP, self.PORT)
        
    def loop(self):
        
        data=self.mr.get()
        if data is not None:
            pass
        