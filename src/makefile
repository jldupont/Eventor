#
# @author Jean-Lou Dupont
#
#
PRJ=eventor
PKG=eventor
BASE=/usr/share

PYTHON=`which python`

all:
	@echo "make install"
	@echo "make clean"
	@echo "make buildsrc"

clean:
	@rm -f $(DESTDIR)$(RBP)/$(PKG)/*.pyc
		
install:
	@install -d $(DESTDIR)$/$(PKG)
	@install -d $(DESTDIR)$/$(PKG)/agents
	@install -d $(DESTDIR)$/$(PKG)/helpers
	@install -d $(DESTDIR)$/$(PKG)/system
	
	## REQUIRED FOR CREATING THE .DEB PACKAGE
	@install -d $(DESTDIR)$(BASE)/applications
	@install -d $(DESTDIR)$(BASE)/icons
	@install -d $(DESTDIR)/usr/local/bin

	
	@install -D $(CURDIR)/$(PKG)/*.py                  $(DESTDIR)$/$(BASE)/$(PKG)/
	@install -D $(CURDIR)/$(PKG)/agents/*.py           $(DESTDIR)$/$(BASE)/$(PKG)/agents
	@install -D $(CURDIR)/$(PKG)/helpers/*.py          $(DESTDIR)$/$(BASE)/$(PKG)/helpers
	@install -D $(CURDIR)/$(PKG)/system/*.py           $(DESTDIR)$/$(BASE)/$(PKG)/system
	

	@install -D $(CURDIR)/*.desktop           $(DESTDIR)$(BASE)/applications/
	@install -D $(CURDIR)/*.png               $(DESTDIR)$(BASE)/icons/ 

	## INSTALL BIN
	@install $(CURDIR)/$(PKG)                 $(DESTDIR)/usr/local/bin/
	
	
	@python -m compileall ${DESTDIR}$/$(PKG)/$(BASE)
	
buildsrc:
	debuild -S