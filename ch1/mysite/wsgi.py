import os
import sys

path = '/home/bizchool/bizhcool.pythonanywhere.com'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from django.core.wsgi import get_wsgi_application
applcation = get_wsgi_application()



