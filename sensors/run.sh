source ../venv/bin/activate
export DJANGO_SETTINGS_MODULE=sensors.settings.production

while :
do
    ./manage.py collect
    ./manage.py clean
    sleep 600
done
