from .common import *

<<<<<<< HEAD
ALLOWED_HOSTS = ['yoongyo.github.io']
=======
ALLOWED_HOSTS = ['http://bizchool.pythonanywhere.com']
>>>>>>> 0e059c53b78f7708726ed241d15f3d4aeb28a974

DEBUG = False

DATABASES = {
    'default': {
<<<<<<< HEAD
        'ENGINE': os.environ.get('DATABASE_ENGINE', 'django.db.backends.sqlite3')
=======
        'ENGINE': os.environ.get('DATABASE_ENGINE', 'django.db.backends.sqlite3'),
>>>>>>> 0e059c53b78f7708726ed241d15f3d4aeb28a974
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
