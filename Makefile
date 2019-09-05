.PHONY : all clean tests install uninstall

MODULE_NAME=ccpatment
VERSION=$(shell grep __version__ $(MODULE_NAME)/__init__.py | awk '{print $$3}' | sed -e s/\'//g)
PYTHON=python3
PIP=pip3

# venv 
# requirements.txt 
# pylint 추가: pylint는 코딩 스타일 체크

all : tests

tests :
	@echo "Running tests $(MODULE_NAME) $(VERSION) ..."
	@$(PYTHON) -m unittest discover -v
	
# test도 했으면 test coverage도 해주면 좋음

