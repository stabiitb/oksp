"""
DJANGO_SETTINGS_MODULE for local development
"""

from .base_settings import *  # pylint: disable=W0614,W0401
from .conf import *  # pylint: disable=W0614,W0401

DEBUG = True

redirecturl = 'http://localhost:8000/account/redirect'
clientid = 'bOSzOhiKUxDAcWTecSSGVN0m1weI7f4RuiKUP4Hw'
clientsecret = 'Y5ASwZPx29bEWZ5AyjCY51br63mqXv6rUSCWdzKRRSFGAQEjrcEX9PGPWwd5hCGRw7grUCg3rL2EgLSvg17Ay8gArxMrZCxTGaQsm4JBFSjnBWG8bY9eOrTk90Tk2b0a'
password = "87asyadg36b26ccncy287292mu7gdsasdjiiecm"

INSTALLED_APPS += [
    'debug_toolbar',
]

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

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
