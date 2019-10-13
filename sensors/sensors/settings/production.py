from .base import *

ALLOWED_HOSTS = [
    'sensors.2li.ch',
    '10.7.89.122',
]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'development_key'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
