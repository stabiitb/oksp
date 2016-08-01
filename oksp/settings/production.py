"""
DJANGO_SETTINGS_MODULE for production
"""

import logging.config

from .base_settings import *  # pylint: disable=W0614,W0401
from .conf import *  # pylint: disable=W0614,W0401

DEBUG = False

ALLOWED_HOSTS = ['*']

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME,
        'USER': DB_USERNAME,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST_NAME,
        'PORT': DB_PORT,
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'oksp_server_'
    }
}

# Logging Configuration
LOGGING_CONFIG = None
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format':
            '%(levelname)s [%(asctime)s] [%(name)s] [%(module)s] [Process:%(process)d] '
            '[Thread:%(thread)d] %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file_django': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
            'formatter': 'verbose'
        },
        'file_application': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/application.log'),
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
    },
    'loggers': {
        '': {
            'handlers': ['file_application'],
            'level': 'INFO',
        },
        'requests': {
            'handlers': ['file_application'],
            'level': 'WARNING',
        },
        'django.security.DisallowedHost': {
            'handlers': ['mail_admins'],
            'level': 'CRITICAL',
            'propagate': False,
        },
        'django': {
            'handlers': ['file_django', 'mail_admins'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
logging.config.dictConfig(LOGGING)

X_FRAME_OPTIONS = 'DENY'
