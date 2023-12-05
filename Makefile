PYTHON=python
SCRIPT=build_template.py

all: build

build:
	$(PYTHON) $(SCRIPT)

.PHONY: build
