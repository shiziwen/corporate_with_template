from .settings import *

#
# Standard Django settings.
#

DEBUG = True
TEMPLATE_DEBUG = DEBUG
WSGI_APPLICATION = 'maykinmedia.wsgi.wsgi_staging.application'
ENVIRONMENT = 'staging'

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = '&&m+pzkmv_23yj2%u6_-p2lko9x7rzr4#s2xzktfm@#t)62s4g'

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

LOGGING['loggers'].update({
    'django': {
        'handlers': ['django'],
        'level': 'WARNING',
        'propagate': True,
    },
})

#
# django-maintenancemode
#
MAINTENANCE_MODE = False
