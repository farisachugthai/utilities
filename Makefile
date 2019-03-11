# Stolen shamelessly from
# https://github.com/sphinx-doc/sphinx/blob/master/Makefile
# Dropped a few targets and added a develop option

PYTHON ?= python3

# Put it first so that "make" without argument is like "make help".
# help:
# 	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: all
all: clean-pyc clean-generated style-check test

.PHONY: clean
clean: clean-pyc clean-pycache clean-generated clean-buildfiles

.PHONY: clean-pyc
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +

.PHONY: clean-pycache
clean-pycache:
	find . -name __pycache__ -exec rm -rf {} +

.PHONY: clean-generated
clean-generated:
	find . -name '.DS_Store' -exec rm -f {} +
	rm -rf .egg-info/
	rm -rf doc/_build/
	rm -rf build/

.PHONY: style-check
style-check:
	@flake8

.PHONY: test
test:
	@$(PYTHON) -m unittest -v $(TEST)


.PHONY: build
build:
	@$(PYTHON) setup.py build

.PHONY: develop
build:
	@$(PYTHON) -m pip install -e .
