from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

if 'test' in sys.argv:
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}

    SOUTH_TESTS_MIGRATE = False
