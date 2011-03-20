'''
Created on 2011-03-20

@author: jldupont
'''
import json

from eventor.system.base import AgentThreadedBase

class CallAgent(AgentThreadedBase):
    
    def __init__(self):
        AgentThreadedBase.__init__(self)
        
    def h_mmsg(self, msg):
        """ msg is JSON encoded
        """
        try:    info=json.loads(msg)
        except: info=None
        
        state=info.get("state", None)
        type=info.get("type", None)
        if type is None or state is None:
            return
        
        number=info.get("from_number", None)
        if type.lower()=="incomingcall":
            if state.lower()=="ringing":
                self.pub("notify", "Incoming call from: %s" % number, "high")
        
