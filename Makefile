SHELL=/bin/bash

.PHONY: run

run: venv
	python3 sensors

test: venv/development
	pytest --cov=. --cov-report=term

venv/development:
	test -d venv || python3 -m venv venv
	( \
	source venv/bin/activate; \
	pip3 install -e .; \
	pip3 install -r requirements/development.txt; \
	)
	touch venv/development

venv:
	test -d venv || python3 -m venv venv
	( \
	source venv/bin/activate; \
	pip3 install .; \
	)

venv/bin/activate: venv
	( \
	source venv/bin/activate; \
	touch venv/bin/activate; \
	)

clean:
	rm -rf venv/
	find . \( -name __pycache__ -o -name "*.pyc" \) -delete
	rm -rf htmlcov/
