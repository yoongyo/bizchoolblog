from .common import *

ALLOWED_HOSTS = ['yoongyo.github.io']

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE', 'django.db.backends.sqlite3')
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
