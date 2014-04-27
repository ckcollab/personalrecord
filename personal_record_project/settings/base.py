import os
import sys

from os.path import abspath, join

### Heroku
ALLOWED_HOSTS = ['*', ]
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DATABASE_NAME = os.environ.get("DATABASE_NAME")
DATABASE_USERNAME = os.environ.get("DATABASE_USERNAME")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
DATABASE_HOST = os.environ.get("DATABASE_HOST", 'localhost')
DATABASE_PORT = os.environ.get("DATABASE_PORT", '')

SENTRY_DSN = os.environ.get("SENTRY_DSN", '')
RAVEN_CONFIG = {
    'dsn': SENTRY_DSN
}

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

SECRET_KEY = 'p*)lzz6km9=$*@3fikdh)-g3pyv2e4)ma$p5i6ri)vghh4rus7'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.static',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
)

ROOT_URLCONF = 'personal_record.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'


BASE_AND_LIBRARY_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'social.apps.django_app.default',

    'django_extensions',
    'gunicorn',
    'raven.contrib.django.raven_compat',
    'south',
    'rest_framework',
    'django_tables2',
)

PERSONAL_RECORD_APPS = (
    'personal_record',
    'home',
    'user_profile',
    'workout',
    'api',
    'ladder'
)

INSTALLED_APPS = BASE_AND_LIBRARY_APPS + PERSONAL_RECORD_APPS

# python-social-auth
AUTHENTICATION_BACKENDS = (
   'social.backends.facebook.FacebookOAuth2',
   'social.backends.google.GoogleOAuth2',
   'social.backends.twitter.TwitterOAuth',
   'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get("SOCIAL_AUTH_FACEBOOK_KEY", None)
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get("SOCIAL_AUTH_FACEBOOK_SECRET", None)
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get("SOCIAL_AUTH_GOOGLE_OAUTH2_KEY", None)
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get("SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET", None)

SOCIAL_AUTH_TWITTER_KEY = os.environ.get("SOCIAL_AUTH_TWITTER_KEY", None)
SOCIAL_AUTH_TWITTER_SECRET = os.environ.get("SOCIAL_AUTH_TWITTER_SECRET", None)

LOGIN_REDIRECT_URL = '/'
AUTH_USER_MODEL = "user_profile.UserProfile"
SOCIAL_AUTH_USER_MODEL = "user_profile.UserProfile"

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
