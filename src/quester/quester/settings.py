# Django settings for quester project.
import logging
import os, sys
# thirdparty settings should be stored in thirdparty_settings.py
from thirdparty_settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
SOCIAL_AUTH_RAISE_EXCEPTIONS = DEBUG

PROJECT_PATH = os.path.normpath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../../'))

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'apps'))

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL = '/login-error/'

ADMINS = (
    ('Olexandr Shalakhin', 'olexandr@shalakhin.com'),
    ('Alexandr Bulanov', 'alexandr.bulanov@djangostars.com'),
    ('Igor Pochechyev', 'pochechyev@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, os.path.abspath(os.path.dirname(__file__)), 'media')

# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_PATH, os.path.abspath(os.path.dirname(__file__)), 'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, os.path.abspath(os.path.dirname(__file__)), "static_dir"),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = 'yn_im1e=e629oh0+e14u5qwyj7@^qp@!_g#%_o9aq)cvtma%ha'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.google.GoogleBackend',
    'social_auth.backends.contrib.github.GithubBackend',
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    # third party stuff
    'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_login_redirect',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'defaults.middleware.InitializeMiddleware',
)

ROOT_URLCONF = 'quester.urls'

WSGI_APPLICATION = 'quester.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, os.path.abspath(os.path.dirname(__file__)), "templates")
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',

    'django.contrib.gis',

    'south',
    'django_countries',
    'social_auth',

    'quest',
    'defaults',
)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
        },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(PROJECT_PATH, 'logs', 'quester.log'),
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 50,
            'formatter': 'standard',
            },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
            },
        }
}

GEOIP_PATH = os.path.join(PROJECT_PATH, 'contrib/geo')

try:
    from local_settings import *
    logging.debug("Local settings file found. Using it.")
    INSTALLED_APPS += LOCAL_INSTALLED_APPS
except ImportError:
    logging.debug("No local settings file. Using global.")
