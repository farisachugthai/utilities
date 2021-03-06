# Stolen shamelessly from
# https://github.com/sphinx-doc/sphinx/blob/master/Makefile
# Dropped a few targets and added a develop option

PYTHON ?= python3

# Put it first so that "make" without argument is like "make help".
# help:
#	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Now all I need is a venv target!
.PHONY: help
help:
	@echo clean
	@echo clean-pyc
	@echo clean-generated
	@echo lint
	@echo build
	@echo test

.PHONY: all
all: clean-pyc clean-generated style-check test build develop

.PHONY: clean
clean: clean-pyc clean-pycache clean-generated clean-ghpages

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
	rm -rf *.egg-info/
	rm -rf docs/_build/
	rm -rf build/
	rm -rf dist/
	rm -rf _sources
	rm -rf .eggs/
	rm -rf html/

.PHONY: clean-git
clean-git:
	git clean -fdx


.PHONY: clean-ghpages
clean-ghpages:
	rm searchindex.js
	rm yarn-error.log
	rm objects.inv

# Fail if any of these files have warnings
.PHONY: lint
lint:
	@$(PYTHON) -m flake8
	shellcheck sh/*.sh


.PHONY: test
test:
	@$(PYTHON) -m unittest -v $(TEST)


.PHONY: build
build:
	@$(PYTHON) setup.py build
	@$(PYTHON) setup.py develop

.PHONY: develop
develop:
	@$(PYTHON) -m pip install -U -e .

.PHONY: whoa
whoa:
	@$(PYTHON) -m pip wheel -w wheel --pre -e .
