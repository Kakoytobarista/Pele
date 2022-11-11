import os
from pathlib import Path
from dotenv import load_dotenv

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


load_dotenv()

sentry_sdk.init(
    dsn=os.getenv('SENTRY_KEY'),
    integrations=[
        DjangoIntegration(),
    ],
    traces_sample_rate=1.0,
    send_default_pii=True
)

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('DJANGO_KEY')

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '0.0.0.0', 'localhost', 'pele.work',
                 'www.pele.work']


INSTALLED_APPS = [
    'api.apps.ApiConfig',
    'modeltranslation',
    'appointment.apps.AppointmentConfig',
    'users.apps.UsersConfig',
    'core.apps.CoreConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_crontab',
    'django_filters',
    'corsheaders',
    'phonenumber_field',
    'django_extensions',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'https://localhost:8000',
    'http://pele.myvnc.com',
    'https://104.248.27.6',
    'http://127.0.0.1:8000',
    'http://pele.work',
)

CSRF_TRUSTED_ORIGINS = ['http://pele.work',
                        'https://104.248.27.6',
                        'https://*.127.0.0.1',
                        'https://*104.248.27.6',
                        'http://pele.myvnc.com',]

ROOT_URLCONF = 'pele.urls'

TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.year.year',
            ],
        },
    },
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':
    ['rest_framework.authentication.TokenAuthentication', ],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PERMISSION_CLASSES':
    ['rest_framework.permissions.IsAuthenticatedOrReadOnly', ],
}

CRONJOBS = [
    ('10 8 * * *', 'core.cron.notification_job', '>> '
     + os.path.join(BASE_DIR, 'logs/notif_appointment.log' + ' 2>&1 ')),
    ('0 0 * * MON', 'core.cron.remove_unusable_appointment_job', '>> '
     + os.path.join(BASE_DIR, 'logs/del_appointment.log' + ' 2>&1 ')),
    ('0 0 * * MON', 'core.cron.clean_log_file_job', '>> '
     + os.path.join(BASE_DIR, 'logs/clean_log_appointment.log' + ' 2>&1 ')),
]

WSGI_APPLICATION = 'pele.wsgi.application'


if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': os.getenv('DB_ENGINE', default='django.db.backends.postgresql'),
            'NAME': os.getenv('DB_NAME', default='postgres'),
            'USER': os.getenv('POSTGRES_USER', default='postgres'),
            'PASSWORD': os.getenv('POSTGRES_PASSWORD', default='postgres'),
            'HOST': os.getenv('DB_HOST', default='db'),
            'PORT': os.getenv('DB_PORT', default='5432')
        }
    }


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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{asctime} {levelname} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'logfile': {
            'class': 'logging.FileHandler',
            'filename': str(BASE_DIR) + '/logs/django.log',
            'formatter': 'verbose',
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'logfile'],

        },
        'appointment': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
            'propagate': True
        },
        'api': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
            'propagate': True
        },
        'core.cron': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
            'propagate': True
        },
    },
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Belgrade'

USE_I18N = True

USE_L1ON = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

get_text = lambda s: s
LANGUAGES = (
    ('sr', get_text('Serbian')),
    ('en', get_text('English')),
)

USE_TZ = True

LOGIN_URL = 'users:login'
LOGIN_REDIRECT_URL = 'appointment:index'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'frizerskiSalonPele@outlook.com'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.getenv('EMAIL_PORT')


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '/static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'users.User'
