PYTHON=python
SCRIPT=build_template.py

all: build serve

build:
	$(PYTHON) $(SCRIPT)

serve:
	cd build && $(PYTHON) -m http.server

.PHONY: all build serve
