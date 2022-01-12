
import os
import django

from django.core.asgi import get_asgi_applicat

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_asgi_applicat()
