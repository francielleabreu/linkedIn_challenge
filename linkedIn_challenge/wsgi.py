import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'linkedIn_challenge.settings')

application = get_wsgi_application()
