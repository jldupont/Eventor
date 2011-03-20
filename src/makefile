#
# @author Jean-Lou Dupont
#
#
PRJ=eventor
PKG=eventor
BASE=/usr/share/eventor
APP_BASE=/usr/share

PYTHON=`which python`

all:
	@echo "make install"
	@echo "make clean"
	@echo "make buildsrc"

clean:
	@rm -f $(DESTDIR)$(BASE)/$(PKG)/*.pyc
		
install:
	@install -d $(DESTDIR)/$(BASE)/$(PKG)
	@install -d $(DESTDIR)/$(BASE)/$(PKG)/agents
	@install -d $(DESTDIR)/$(BASE)/$(PKG)/res
	@install -d $(DESTDIR)/$(BASE)/$(PKG)/system
	
	## REQUIRED FOR CREATING THE .DEB PACKAGE
	@install -d $(DESTDIR)$(APP_BASE)/applications
	@install -d $(DESTDIR)$(APP_BASE)/icons
	@install -d $(DESTDIR)/usr/bin
	
	@install -D $(CURDIR)/$(PKG)/*.py                  $(DESTDIR)/$(BASE)/$(PKG)/
	@install -D $(CURDIR)/$(PKG)/agents/*.py           $(DESTDIR)/$(BASE)/$(PKG)/agents
	@install -D $(CURDIR)/$(PKG)/res/*.*               $(DESTDIR)/$(BASE)/$(PKG)/res
	@install -D $(CURDIR)/$(PKG)/system/*.py           $(DESTDIR)/$(BASE)/$(PKG)/system
	

	@install -D $(CURDIR)/*.desktop                    $(DESTDIR)$(APP_BASE)/applications
	@install -D $(CURDIR)/$(PKG)/res/*.png             $(DESTDIR)$(APP_BASE)/icons 

	## INSTALL BIN
	@install $(CURDIR)/*.sh                            $(DESTDIR)/usr/bin
	@install $(CURDIR)/*.py                            $(DESTDIR)/usr/bin
	
	
	@python -m compileall ${DESTDIR}/$(BASE)/$(PKG)
	
buildsrc:
	debuild -S