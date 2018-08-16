from .base import *

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

DEBUG = False
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']

# WSGI application
WSGI_APPLICATION = 'config.wsgi.deploy.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



<<<<<<< HEAD
MEDIA_URL = "https://bizchool.pythonanywhere.com/media/"
# MEDIA_ROOT = os.path.join(BASE_DIR, 'mysite', 'media')
=======
MEDIA_URL = '/media/'
>>>>>>> c31f123974ba6a7060776205ce6329f0391b283d
MEDIA_ROOT = '/home/bizchool/bizchoolblog/ch1/mysite/mysite/media/django-summernote'

STATIC_URL = "https://bizchool.pythonanywhere.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
 os.path.join(BASE_DIR, 'staticfiles'),
]


