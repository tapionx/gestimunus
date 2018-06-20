"""
Django settings for gestimunus project.

Generated by 'django-admin startproject' using Django 1.11.13.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

from getenv import env
from datetime import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # 'settings',
    # 'tools',
    # 'django_adminlte_theme',
    # 'django_adminlte',
    'django_admin_bootstrapped',
    # 'adminlte',
    # 'adminlte.apps.AdminlteConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rangefilter',
    'export_action',
    'fullcalendar',
    'settings',
    'tools',
    'tinymce',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gestimunus.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'gestimunus/templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'adminlte.utils.admin_config',
            ],
        },
    },
]


WSGI_APPLICATION = 'gestimunus.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

#DATABASES = {
    #'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #}
#}

DATABASES = {
        'default': {
                          'ENGINE': 'django.db.backends.postgresql_psycopg2',
                          'NAME': env("DBNAME"),
                          'USER': env("DBUSER"),
                          'PASSWORD': env("DBPASSWD"),
                          'HOST': env("DBHOST"),
                          'PORT': '',
                      }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'
# LANGUAGE_CODE = 'it-it'

#Model Translation
gettext = lambda s: s
LANGUAGES = (
    ('it', gettext('Italian')),
    ('en', gettext('English')),
)
MODELTRANSLATION_LANGUAGES = ('it', 'en')
MODELTRANSLATION_DEFAULT_LANGUAGE = 'it'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Europe/Rome'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_UPLOAD = 'uploads/' + datetime.now().strftime("%Y")+'/'+datetime.now().strftime("%m")+'/'+datetime.now().strftime("%d")+'/'
# MEDIA_ROOT = [ os.path.join(BASE_DIR, "uploads/") ]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "gestimunus/static/"),
]


## FULLCALENDAR

# FULLCALENDAR = {
    # 'css_url': os.path.join(BASE_DIR, 'gestimunus/static/admin/bootstrap/css/bootstrap.css.map'), # 'static/admin/bootstrap/css/bootstrap.css.map',
    # 'print_css_url': <path_or_url_to_print_css_file>,
    # 'javascript_url': <path_or_url_to_javascript_file>,
    # 'jquery_url': <path_or_url_to_jquery_file>,
    # 'jquery_ui_url': <path_or_url_to_jquery_ui_file>,
# }

## LOG CONFIG
# import logging.config
# import os
# from django.utils.log import DEFAULT_LOGGING

# Disable Django's logging setup
LOGGING_CONFIG = None

LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(pathname)s:%(lineno)s] %(message)s',
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'logging.NullHandler',
        },
        'logfile': {
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': "gestimunus/static/logs/gestimunus.log",
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'verbose',
        },
        'console':{
            'level':'INFO',
            'class':'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers':['console'],
            'propagate': True,
            'level':'WARN',
        },
        # 'django.request': {
        #     'handlers':['console'],
        #     'propagate': True,
        #     'level':'WARN',
        # },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'textlogger': {
            'handlers': ['console', 'logfile'],
            'level': 'INFO',
        },
    }
}

import logging.config
logging.config.dictConfig(LOGGING)
