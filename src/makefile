#
# @author Jean-Lou Dupont
#
#
PRJ=eventor
PKG=eventor

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
	
	@install -D $(CURDIR)/$(PKG)/*.py                  $(DESTDIR)$/$(PKG)/
	@install -D $(CURDIR)/$(PKG)/agents/*.py           $(DESTDIR)$/$(PKG)/agents
	@install -D $(CURDIR)/$(PKG)/helpers/*.py          $(DESTDIR)$/$(PKG)/helpers
	@install -D $(CURDIR)/$(PKG)/system/*.py           $(DESTDIR)$/$(PKG)/system
	
	@python -m compileall ${DESTDIR}$/$(PKG)
	
buildsrc:
	debuild -S