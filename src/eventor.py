"""
    Multicast bridge over Dbus
    
    @author: jldupont
    @date: March 2011
"""
APP_NAME="eventor"
APP_ICON = "eventor"
ICON_PATH="/usr/share/icons/"
ICON_FILE="eventor.png"
LOG_PATH="~/eventor.log"
HELP_URL="http://www.systemical.com/doc/opensource/eventor"
TIME_BASE=250  ##milliseconds
TICKS_SECOND=1000/TIME_BASE
       

import os
import sys

## For development environment
ppkg=os.path.abspath( os.getcwd() +"/eventor")
if os.path.exists(ppkg):
    sys.path.insert(0, ppkg)

import gobject
import dbus.glib
from dbus.mainloop.glib import DBusGMainLoop
import gtk

gobject.threads_init()
dbus.glib.init_threads()
DBusGMainLoop(set_as_default=True)

from app.system import mswitch

## ------------------------------
## configurables
from app.agents.tray import TrayAgent
_ta=TrayAgent(APP_NAME, ICON_PATH, ICON_FILE)

from app.agents.logger import LoggerAgent
_la=LoggerAgent(APP_NAME, LOG_PATH)
_la.start()


from app.agents import adbus
from app.agents import mb
from app.agents import heart

from app.agents.ui import UiAgent
ui=UiAgent(HELP_URL, TICKS_SECOND)
gobject.timeout_add(TIME_BASE, ui.tick)

gtk.main()
