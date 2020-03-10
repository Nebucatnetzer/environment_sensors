nohub gunicorn sensors.wsgi:application --bind 0.0.0.0:80 --workers 3
nohub ./collector.sh
