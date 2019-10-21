source ../venv/bin/activate
export DJANGO_SETTINGS_MODULE=sensors.settings.production

while :
do
    ./manage.py collect
    sleep 600
done
