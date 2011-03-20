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
	@install -d $(DESTDIR)/$(BASE)/$(PKG)
	@install -d $(DESTDIR)/$(BASE)/$(PKG)/agents
	@install -d $(DESTDIR)/$(BASE)/$(PKG)/res
	@install -d $(DESTDIR)/$(BASE)/$(PKG)/system
	
	## REQUIRED FOR CREATING THE .DEB PACKAGE
	@install -d $(DESTDIR)$(BASE)/applications
	@install -d $(DESTDIR)$(BASE)/icons
	@install -d $(DESTDIR)/usr/local/bin

	
	@install -D $(CURDIR)/$(PKG)/*.py                  $(DESTDIR)$/$(BASE)/$(PKG)/
	@install -D $(CURDIR)/$(PKG)/agents/*.py           $(DESTDIR)$/$(BASE)/$(PKG)/agents
	@install -D $(CURDIR)/$(PKG)/res/*.*               $(DESTDIR)$/$(BASE)/$(PKG)/res
	@install -D $(CURDIR)/$(PKG)/system/*.py           $(DESTDIR)$/$(BASE)/$(PKG)/system
	

	@install -D $(CURDIR)/*.desktop                    $(DESTDIR)$(BASE)/applications/
	@install -D $(CURDIR)/$(PKG)/*.png                 $(DESTDIR)$(BASE)/icons/ 

	## INSTALL BIN
	@install $(CURDIR)/$(PKG)                 $(DESTDIR)/usr/local/bin/
	
	
	@python -m compileall ${DESTDIR}$/$(PKG)/$(BASE)
	
buildsrc:
	debuild -S