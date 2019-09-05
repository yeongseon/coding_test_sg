.PHONY : all clean tests install uninstall

MODULE_NAME=ccpatment
VERSION=$(shell grep __version__ $(MODULE_NAME)/__init__.py | awk '{print $$3}' | sed -e s/\'//g)
PYTHON=python3
PIP=pip3

all : tests

tests :
	@echo "Running tests $(MODULE_NAME) $(VERSION) ..."
	@$(PYTHON) -m unittest discover -v

