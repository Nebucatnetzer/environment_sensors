export DJANGO_SETTINGS_MODULE=sensors.settings.production
export DJANGO_DEBUG=False
export DJANGO_SECRET_KEY=foo
./manage.py makemigrations
./manage.py migrate
gunicorn sensors.wsgi:application --bind 0.0.0.0:8000 --workers 3 &
./collector.sh &
