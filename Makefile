# Variables
SOURCE = margatsni

# Functions
define clean
	rm -rf *.egg-info .pytest_cache build dist
	find . -name "*.pyc" | xargs rm -f
	find . -name "*.pyo" | xargs rm -f
	find . -name __pycache__ | xargs rm -rf
	rm -f *.spec
endef

# Targets
all: lint
compile: clean pyinstaller
publish: clean lint upload
	$(call clean)

clean:
	$(call clean)

deps:
	pip3 install -U pip
	pip3 install -r requirements.txt

lint:
	@echo Searching for unused imports...
	importchecker $(SOURCE) | grep -v __init__ || true
	@echo

format:
	@echo Formatting source code using black
	black $(SOURCE) ftest hooks scripts test
	@echo

upload:
	python setup.py sdist bdist_wheel
	twine upload dist/*
