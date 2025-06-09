# Project management tasks.

VENV = .venv
PYTHON = source $(VENV)/bin/activate && python
PYTHONPATH := $(PYTHONPATH):$(shell pwd)

$(VENV)/.make-update: requirements-dev.txt
	python -m venv $(VENV)
	bash -c "source $(VENV)/bin/activate && python -m pip install -r requirements-dev.txt"
	touch $@


.PHONY: dev
dev: $(VENV)/.make-update


.PHONY: test
test: dev
	PYTHONPATH=$(PYTHONPATH) . $(VENV)/bin/activate && pytest
