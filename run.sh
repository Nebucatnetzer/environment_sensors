source ./venv/bin/activate
export DJANGO_SETTINGS_MODULE=sensors.settings.production
./manage.py migrate
./collector.sh &
gunicorn sensors.wsgi:application --bind 0.0.0.0:8000 --workers 4
