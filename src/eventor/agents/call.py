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
        
        type=info.get("type", None)
        if type is None:
            return

        handler=getattr(self, "h_%s" % type, None)
        if handler is None:
            return
        
        handler(self, info)
        

    def h_incomingcall(self, info):
        """
        Handler for type: incomingCall
        """
        state=info.get("state", None)
        number=info.get("from_number", None)
        if state.lower()=="ringing":
            self.pub("notify", "Incoming call from: %s" % number, "high")
        
    def h_sms(self, info):
        """
        Handler for type: "sms"
        """
        number=info.get("from_number", None)
        self.pub("notify", "SMS from: %s" % number, "high")
        