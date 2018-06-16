"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""
<<<<<<< HEAD

=======
>>>>>>> 0e059c53b78f7708726ed241d15f3d4aeb28a974
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings.prod")

application = get_wsgi_application()
