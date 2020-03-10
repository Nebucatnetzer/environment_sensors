SHELL=/bin/bash

.PHONY: run

run: venv/production
	( \
	source venv/bin/activate; \
	./run.sh; \
	)

test: venv/development
	( \
	source venv/bin/activate; \
	export DJANGO_SETTINGS_MODULE=sensors.settings.production; \
	pytest --nomigrations --cov=. --cov-report=html sensors/; \
	)

migrations:
	( \
	export DJANGO_SETTINGS_MODULE=sensors.settings.development; \
	./manage.py makemigrations collector; \
	)

venv/development:
	test -d venv || python3 -m venv venv --system-site-packages
	( \
	source venv/bin/activate; \
	pip3 install -r requirements/development.txt; \
	)
	touch venv/development

venv/production:
	test -d venv || python3 -m venv venv --system-site-packages
	( \
	source venv/bin/activate; \
	pip3 install -Ur requirements/production.txt; \
	touch venv/bin/activate: \
	)

clean:
	rm -rf venv/
	find . \( -name __pycache__ -o -name "*.pyc" \) -delete
	rm -rf htmlcov/
