# -*- coding: utf-8 -*-
"""
Django settings for starlight_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#yt2*mvya*ulaxd+6jtr#%ouyco*2%3ngb=u-_$44j^86g0$$3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'bootstrapform',
    'snowpenguin.django.recaptcha3',
    'rest_framework',
    'storages',
    'magi',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'magi.middleware.languageFromPreferences.LanguageFromPreferenceMiddleWare',
    'magi.middleware.httpredirect.HttpRedirectMiddleware',
)

ROOT_URLCONF = 'starlight_project.urls'

WSGI_APPLICATION = 'starlight_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

SITE = 'starlight'

AUTHENTICATION_BACKENDS = ('magi.backends.AuthenticationBackend',)

DEBUG_PORT = 8000

from django.utils.translation import ugettext_lazy as _

LANGUAGES = (
    ('en', _('English')),
    ('es', _('Spanish')),
    ('zh-hans', _('Simplified Chinese')),
    ('ru', _('Russian')),
    ('it', _('Italian')),
    ('fr', _('French')),
    ('de', _('German')),
    ('pl', _('Polish')),
    ('ja', _('Japanese')),
    ('kr', _('Korean')),
    ('id', _('Indonesian')),
    ('vi', _('Vietnamese')),
    ('zh-hant', _('Traditional Chinese')),
    ('pt', _('Portuguese')),
    ('pt-br', _('Brazilian Portuguese')),
    ('tr', _('Turkish')),
    ('th', _('Thai')),
    ('uk', _('Ukrainian')),
)

NATIVE_LANGUAGES = (
    ('en', u'English'),
    ('es', u'Español'),
    ('zh-hans', u'简体中文'),
    ('ru', u'Русский'),
    ('it', u'Italiano'),
    ('fr', u'Français'),
    ('de', u'Deutsch'),
    ('pl', u'polski'),
    ('ja', u'日本語'),
    ('kr', u'한국어'),
    ('id', u'Indonesia'),
    ('vi', u'Tiếng Việt Nam'),
    ('zh-hant', u'繁體中文'),
    ('pt', u'Português'),
    ('pt-br', u'Português Brasileiro'),
    ('tr', u'Türkçe'),
    ('th', u'ไทย'),
    ('uk', u'Українська'),
)

LANGUAGE_CODE = 'en'

LOCALE_PATHS = [
  os.path.join(BASE_DIR, 'magi/locale'),
]

STATIC_UPLOADED_FILES_PREFIX = None

CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = r'^/api/.*$'

LOGIN_REDIRECT_URL = '/'
LOG_EMAIL = 'emails-log@schoolido.lu'
PASSWORD_EMAIL = 'password@schoolido.lu'
AWS_SES_RETURN_PATH = 'contact@starlight.academy'

RECAPTCHA_PRIVATE_KEY = ''
RECAPTCHA_PUBLIC_KEY = ''
RECAPTCHA_DEFAULT_ACTION = 'generic'
RECAPTCHA_SCORE_THRESHOLD = 0.5

FAVORITE_CHARACTERS = []
STAGE_GIRLS_NAMES = {}
STAFF_CONFIGURATIONS = {}
SCHOOLS = {}
IMPORTABLE_FIELDS = {}
VOICE_ACTRESSES = {}
MAX_STATISTICS = {}

MAX_WIDTH = 1200
MAX_HEIGHT = 1200
MIN_WIDTH = 300
MIN_HEIGHT = 300

STATIC_FILES_VERSION = ''

try:
    from generated_settings import *
except ImportError, e:
    pass
try:
    from local_settings import *
except ImportError, e:
    pass

INSTALLED_APPS = list(INSTALLED_APPS)
INSTALLED_APPS.append(SITE)

LOCALE_PATHS = list(LOCALE_PATHS)
LOCALE_PATHS.append(os.path.join(BASE_DIR, SITE, 'locale'))

if STATIC_UPLOADED_FILES_PREFIX is None:
    STATIC_UPLOADED_FILES_PREFIX = SITE + '/static/uploaded/' if DEBUG else 'u/'
