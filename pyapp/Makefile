# Project management tasks.

VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

$(VENV)/.make-update: requirements-dev.txt
	python -m venv $(VENV)
	$(PIP) install -r requirements-dev.txt
	touch $@

.PHONY: dev
dev: $(VENV)/.make-update

.PHONY: test
test: dev
	PYTHONPATH=pyapp:. . $(VENV)/bin/activate && pytest tests/
