"""
    MediaKeys Dbus Agent
    
    Messages Generated:
    - "mk_key_press" (key, source, priority)
        priority: 1 -> low, 5 -> high
    
    Created on 2010-10-22
    @author: jldupont
"""
import dbus.service
    
from eventor.system.base import AgentThreadedBase
#pyfrom eventor.system import mswitch

__all__=[]


class SignalTx(dbus.service.Object):

    PATH="/Track"
    
    def __init__(self, agent):
        dbus.service.Object.__init__(self, dbus.SystemBus(), self.PATH)
        self.agent=agent
        
    @dbus.service.signal(dbus_interface="com.systemical.eventor", signature="s")
    def Msg(self, msg):
        pass


class DbusAgent(AgentThreadedBase):
    
    def __init__(self):
        AgentThreadedBase.__init__(self)

        self.stx=SignalTx(self)
        
    def h_mmsg(self, msg):
        self.stx.Track(msg)
                   
_=DbusAgent()
_.start()
