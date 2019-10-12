SHELL=/bin/bash

.PHONY: run

run: venv
	./sensors

test:
	pytest --cov=. --cov-report=html

developement:
	python3 -m venv venv
	( \
	source venv/bin/activate; \
	pip3 install -r requirements/development.txt; \
	)

venv:
	python3 -m venv venv
	( \
	source venv/bin/activate; \
	pip3 install -r requirements/base.txt; \
	)

clean:
	rm -rf venv/
	find . \( -name __pycache__ -o -name "*.pyc" \) -delete
	rm -rf htmlcov/
