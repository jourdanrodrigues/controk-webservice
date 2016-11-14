from os import environ, getenv, path
from sys import argv

from dj_database_url import config as db_config
from re import match

BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))

# Start ".env" file reader
# https://gist.github.com/bennylope/2999704
try:
    with open(path.join(BASE_DIR, '.env')) as f:  # pragma: no cover
        content = f.read()
except IOError:
    content = ''

for line in content.splitlines():  # pragma: no cover
    m1 = match(r'\A(?P<key>[A-Za-z_0-9]+)=(?P<value>.*)\Z', line)
    if m1:
        environ.setdefault(**m1.groupdict())
# End ".env" file reader

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '44m*-49@=blr^dmjxn2iq2@ebqpoen#$w%6r+%l-b5!_ups3k1'

DEBUG = bool(int(getenv('DEBUG', 0)))

TEST = 'test' in argv

ALLOWED_HOSTS = getenv('ALLOWED_HOSTS', '*' if DEBUG else '').split(',')

LOCAL_APPS = [
    'controk_webservice.addresses',
    'controk_webservice.clients',
    'controk_webservice.employees',
    'controk_webservice.stock',
    'controk_webservice.suppliers',
    'controk_webservice.users'
]

THIRD_APPS = [
    'corsheaders',
    'rest_framework',
    'rest_framework_swagger',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
] + THIRD_APPS + LOCAL_APPS

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DEBUG and bool(getenv('QUERIES_LOG')):  # pragma: no cover
    MIDDLEWARE += ['assets.middleware.query.QueriesLog']

ROOT_URLCONF = 'controk_webservice.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

FIXTURE_DIRS = [
    path.join(BASE_DIR, 'assets/fixtures')
]

LOCALE_PATHS = [
    path.join(BASE_DIR, 'locale'),
]

WSGI_APPLICATION = 'controk_webservice.wsgi.application'

DATABASES = {'default': db_config()}
# DB_URL=postgres://{USER}:{PASSWORD}@{HOST}/{DB_NAME}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

STATIC_URL = '/static/'

STATIC_ROOT = path.join(BASE_DIR, 'static')

AUTH_USER_MODEL = 'users.User'

CORS_ORIGIN_ALLOW_ALL = True
