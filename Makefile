SHELL=/bin/bash

.PHONY: run

run: venv/production
	( \
	source venv/bin/activate; \
	export DJANGO_SETTINGS_MODULE=sensors.settings.production; \
	./sensors/manage.py makemigrations; \
	./sensors/manage.py migrate; \
	./sensors/manage.py runserver 0:8000; \
	)

test: venv/development
	( \
	source venv/bin/activate; \
	export DJANGO_SETTINGS_MODULE=sensors.settings.development; \
	pytest --nomigrations --cov=. --cov-report=html sensors/; \
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
