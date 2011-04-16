'''
    IPReg Agent

    Registers service at start-up and at most once per day

    Created on 2011-04-15
    @author: jldupont
'''
from eventor.system.base import AgentThreadedBase
from eventor.system.network import get_ip


class IPReg(AgentThreadedBase):

    API_SET="http://services.systemical.com/ipreg/v1/%s/%s"
    
    def __init__(self):
        AgentThreadedBase.__init__(self)
        try:
            self.ip=get_ip()[0]
        except:
            self.ip=None

    def h___tick__(self, ticks_second, 
                        tick_second, tick_min, tick_hour, tick_day, 
                        sec_count, min_count, hour_count, day_count):
        pass
    


_=IPReg()
_.start()
