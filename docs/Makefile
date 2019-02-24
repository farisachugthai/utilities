# Minimal makefile for Sphinx documentation

# Grabbed a few useful lines from:
# https://raw.githubusercontent.com/python/cpython/3.7/Doc/Makefile

# You can set these variables from the command line.
PYTHON        = python3
SPHINXBUILD   = sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build
# CONFDIR		  = "$(PWD)"
SPHINXOPTS    =
# -c "$(CONFDIR)" isn't working in sphinx opts

# User-friendly check for sphinx-build
ifeq ($(shell which $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 1)
$(error The "$(SPHINXBUILD)" command was not found. Make sure you have Sphinx installed, then set the SPHINXBUILD environment variable to point to the full path of the "$(SPHINXBUILD)" executable. Alternatively you can add the directory with the executable to your PATH. If you don\'t have Sphinx installed, grab it from http://sphinx-doc.org/)
endif

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile htmlview

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

htmlview: html
	 $(PYTHON) -c "import webbrowser; webbrowser.open('_build/html/index.html')"
