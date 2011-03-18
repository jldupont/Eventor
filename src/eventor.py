"""
    Eventor
        
    14 Feb 2011: added "playing now" dbus signal
        
    Created on 2010-10-21
    @author: jldupont
"""
import sys

APP_NAME="Eventor"
ICON_NAME="eventor.png"
HELP_URL="http://www.systemical.com/doc/opensource/eventor"
TIME_BASE=5000

###<<< DEVELOPMENT MODE SWITCHES
MSWITCH_OBSERVE_MODE=False
MSWITCH_DEBUGGING_MODE=False
MSWITCH_DEBUG_INTEREST=False
DEV_MODE=True
###>>>

import gobject, dbus.glib, gtk
from dbus.mainloop.glib import DBusGMainLoop

gobject.threads_init()  #@UndefinedVariable
dbus.glib.init_threads()
DBusGMainLoop(set_as_default=True)

from eventor.system import base as base
base.debug=DEV_MODE
base.debug_interest=MSWITCH_DEBUG_INTEREST

from eventor.system import mswitch #@UnusedImport
mswitch.observe_mode=MSWITCH_OBSERVE_MODE
mswitch.debugging_mode=MSWITCH_DEBUGGING_MODE

from eventor.agents.notifier import notify, NotifierAgent #@Reimport
from eventor.agents.clock import Clock #@Reimport

def main(debug=False):
    try:
        
        from jld_scripts.res import get_res_path
        icon_path=get_res_path()
        
        from eventor.agents.eventor_tray import TrayAgent
        _ta=TrayAgent(APP_NAME, icon_path, ICON_NAME, HELP_URL)

        import eventor.agents.adbus #@UnusedImport

        
        _na=NotifierAgent(APP_NAME, ICON_NAME)
        _na.start()
        
        clk=Clock(TIME_BASE)
        gobject.timeout_add(TIME_BASE, clk.tick)
        
        mswitch.publish("__main__", "debug", debug)
        
        gtk.main()
    except KeyboardInterrupt:
        mswitch.quit()
        sys.exit(1)        
        
    except Exception,e:
        notify(APP_NAME, "There was an error: %s" % e)
        mswitch.quit()
        sys.exit(1)

