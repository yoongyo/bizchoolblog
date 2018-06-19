import os
import sys
from django.core.wsgi import get_wsgi_application

"""
path = '/home/bizchool/bizhcool.pythonanywhere.com'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings.prod")

from django.core.wsgi import get_wsgi_application
applcation = get_wsgi_application()
"""
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings.prod")

application = get_wsgi_application()

