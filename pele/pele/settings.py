import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-$wpx-y0n%_+_7*hkkg0(zq!og0kup5&=4ek&zoz@5w(kup10c6'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '0.0.0.0', 'pele.work',
                 'www.pele.work', '54.91.26.135', 'ec2-54-91-26-135.compute-1.amazonaws.com']

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
    'django_filters',
    'corsheaders',
    'phonenumber_field',
    'django_extensions',
    'django_celery_results',
    'django_celery_beat',
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

CSRF_TRUSTED_ORIGINS = ["https://pele.work", "https://www.pele.work"]

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
    ('10 8 * * *', 'core.cron.notification_job', '>> ' + os.path.join(BASE_DIR,
     'logs/notif_appointment.log' + ' 2>&1 ')),
    ('0 0 * * MON', 'core.cron.remove_unusable_appointment_job', '>> ' + os.path.join(BASE_DIR,
     'logs/del_appointment.log' + ' 2>&1 ')),
    ('0 0 * * MON', 'core.cron.clean_log_file_job', '>> ' + os.path.join(BASE_DIR,
     'logs/clean_log_appointment.log' + ' 2>&1 ')),
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

LANGUAGES = (
    ('sr', 'Serbian'),
    ('en', 'English'),
)

USE_TZ = True

LOGIN_URL = 'users:login'
LOGIN_REDIRECT_URL = 'appointment:index'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'frizerskiSalonPele@outlook.com'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_HOST_USER = 'frizerskiSalonPele@outlook.com'
EMAIL_HOST_PASSWORD = 'qwe123!@#P{}'
EMAIL_PORT = '587'

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_DIRS = [
    BASE_DIR / "staticfiles",

]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'users.User'

# CELERY

CELERY_BROKER_URL = 'redis://0.0.0.0:16379/0'
CELERY_RESULT_BACKEND = 'django-db'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://0.0.0.0:16379/1',
    }
}

CELERY_CACHE_BACKEND = 'default'

CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
