from .common import *


DEBUG = False
SECRET_KEY = 'u+ce2p()2-$y1!akctmb4#q*=n05*k=xqr+&mx8n1x7(2(ywr3'

ALLOWED_HOSTS = ['bizchool.pythonanywhere.com']

MEDIA_URL = 'https://bizchool.pythonanywhere.com/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mysite', 'media')

STATIC_URL = "https://bizchool.pythonanywhere.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'mysite', 'staticfiles')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""
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
"""
