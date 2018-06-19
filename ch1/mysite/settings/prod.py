from .common import *



DEBUG = False

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_secret("SECRET_KEY")

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
