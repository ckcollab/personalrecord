import os
import sys

from os.path import abspath, join

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

### Heroku

ALLOWED_HOSTS = ['*', ]
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

### Heroku

MANAGERS = ADMINS

DATABASE_NAME = os.environ.get("DATABASE_NAME")
DATABASE_USERNAME = os.environ.get("DATABASE_USERNAME")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
DATABASE_HOST = os.environ.get("DATABASE_HOST", 'localhost')
DATABASE_PORT = os.environ.get("DATABASE_PORT", '')
SENTRY_DSN = os.environ.get("SENTRY_DSN", '')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USERNAME,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
    }
}

# Include other apps
PROJECT_ROOT = abspath(join(os.path.curdir, "personal_record_project"))
sys.path.append(join(PROJECT_ROOT, 'apps'))

# Directories
PROJECT_DIR = abspath(join(PROJECT_ROOT, ".."))
#MEDIA_ROOT = abspath(join(PROJECT_ROOT, 'media'))
#MEDIA_URL = '/media/'
STATIC_ROOT = abspath(join(PROJECT_ROOT, 'collected_static'))
STATIC_URL = '/static/'

STATICFILES_DIRS = (abspath(join(PROJECT_ROOT, 'static')),)

TEMPLATE_DIRS = (abspath(join(PROJECT_ROOT, 'templates')),)

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = False

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'p*)lhh6km9=$*@3fikdh)-g3pyv2e4)ma$p5i6ri)vghh4rus7'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    'django.contrib.auth.context_processors.auth',
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'personal_record.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'personal_record.wsgi.application'


BASE_AND_LIBRARY_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'django_extensions',
    'gunicorn',
    'south',
)

PERSONAL_RECORD_APPS = (
    'personal_record',
    'home',
    'user_profile',
)

INSTALLED_APPS = BASE_AND_LIBRARY_APPS + PERSONAL_RECORD_APPS

# allauth
ACCOUNT_AUTHENTICATION_METHOD = "username_email"

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'SCOPE': ['email'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'METHOD': 'js_sdk',
        'LOCALE_FUNC': lambda request: 'en_US'
    }
}

LOGIN_REDIRECT_URL = '/'
AUTH_USER_MODEL = "user_profile.UserProfile"

# Nose
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        #'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        #'sentry': {
        #    'level': 'ERROR',
        #    'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        #},
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}
