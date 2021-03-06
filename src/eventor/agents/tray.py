"""
    Tray Icon Agent
        
    Created on 2010-08-16
    @author: jldupont
"""
__all__=["TrayAgent"]

import os
import gtk #@UnusedImport
import gtk.gdk
import eventor.system.mswitch as mswitch

class AppPopupMenu:
    def __init__(self, app):
        self.item_exit = gtk.MenuItem( "exit", True)
        self.item_show = gtk.MenuItem( "show", True)
        self.item_show.connect( 'activate', app.show)        
        self.item_exit.connect( 'activate', app.exit)

        self.menu = gtk.Menu()
        self.menu.append( self.item_show)
        self.menu.append( self.item_exit)        
        self.menu.show_all()

    def show_menu(self, button, time):
        self.menu.popup( None, None, None, button, time)
        

class AppIcon(object):
    
    def __init__(self, icon_path, icon_file):
        self.icon_path=icon_path
        self.icon_file=icon_file
        self.curdir=os.path.abspath( os.path.dirname(__file__) )
        self.twodirup=os.path.abspath( os.path.join(self.curdir, "..", "..") )
    
    def getIconPixBuf(self): 
        try:
            ipath=self.icon_path+"/"+self.icon_file
            pixbuf = gtk.gdk.pixbuf_new_from_file( ipath )
        except:
            ipath=os.path.join(self.twodirup, self.icon_file)
            pixbuf = gtk.gdk.pixbuf_new_from_file( ipath )
                      
        return pixbuf.scale_simple(24,24,gtk.gdk.INTERP_BILINEAR)



class TrayAgent(object):
    def __init__(self, app_name, icon_path, icon_file):
        
        self.app_name=app_name
        self.popup_menu=AppPopupMenu(self)
        
        self.tray=gtk.StatusIcon()
        self.tray.set_visible(True)
        self.tray.set_tooltip(self.app_name)
        #self.tray.connect('activate', self.do_popup_menu_activate)
        self.tray.connect('popup-menu', self.do_popup_menu)
        
        scaled_buf = AppIcon(icon_path, icon_file).getIconPixBuf()
        self.tray.set_from_pixbuf( scaled_buf )
        
    def do_popup_menu_activate(self, statusIcon):
        timestamp=gtk.get_current_event_time()
        print timestamp
        self.popup_menu.show_menu(None, int(timestamp))
        
    def do_popup_menu(self, status, button, time):
        self.popup_menu.show_menu(button, time)

    def show(self, *_):
        print "menu: show"
        mswitch.publish(self, "__show__")

    def exit(self, *p):
        print "menu: exit"
        mswitch.publish(self, "__quit__")


#_app=App()
