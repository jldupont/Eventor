"""
    MediaKeys Dbus Agent
    
    Created on 2010-10-22
    @author: jldupont
    
    e.g.
    signal sender=:1.122 -> dest=(null destination) serial=2 
    path=/Events; 
    interface=com.systemical.eventor; member=Msg
       string "{"type":"incomingCall","state":"RINGING","from_number":"15146750877","phone":"15145545655"}"
   
"""
import dbus.service
    
from eventor.system.base import AgentThreadedBase
#pyfrom eventor.system import mswitch

__all__=[]


class SignalTx(dbus.service.Object):

    PATH="/Events"
    
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
        self.stx.Msg(msg)
                   
_=DbusAgent()
_.start()
