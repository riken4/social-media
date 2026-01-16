import sys
path = '/home/riken4/social-media'
if path not in sys.path:
    sys.path.append(path)

from django.core.wsgi import get_wsgi_application
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'social_media.settings'

application = get_wsgi_application()
