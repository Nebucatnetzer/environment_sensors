SHELL=/usr/bin/env bash

.PHONY: run

run: venv
	( \
	./run.sh; \
	)

test: venv
	( \
	export DJANGO_SETTINGS_MODULE=sensors.settings.production; \
	pytest --nomigrations --cov=. --cov-report=html sensors/; \
	)

migrations:
	( \
	export DJANGO_SETTINGS_MODULE=sensors.settings.development; \
	./manage.py makemigrations collector; \
	)

venv:
	nix build .#venv -o venv

clean:
	rm venv
	find . \( -name __pycache__ -o -name "*.pyc" \) -delete
	rm -rf htmlcov/
