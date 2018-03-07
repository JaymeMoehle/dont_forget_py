"""
WSGI config for dont_forget_py project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
#import sys

from django.core.wsgi import get_wsgi_application

#sys.path.insert(0, '/opt/python/current/app')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dont_forget_py.settings")

application = get_wsgi_application()
