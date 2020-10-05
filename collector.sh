while :
do
    source ./venv/bin/activate
    ./manage.py collect
    ./manage.py clean
    sleep 300
done
