PY?=python

BASEDIR=$(CURDIR)
SRCDIR=$(BASEDIR)/src

APP=thesaurus
VENVHOME=~/virtualenvs
VENVDIR=$(VENVHOME)/$(APP)
VENVBIN=virtualenv
PYTHON_BIN=$(VENVDIR)/bin/python
PIP_BIN=$(VENVDIR)/bin/pip

clean:
	[ ! -d $(VENVDIR) ] || rm -rf $(VENVDIR)

venv:
	test -d $(VENVHOME) || mkdir -p $(VENVHOME)
	test -d $(VENVDIR)  || $(VENVBIN) $(VENVDIR)
	$(PIP_BIN) install --upgrade pip

install: venv
	$(PIP_BIN) install -r requirements.txt
