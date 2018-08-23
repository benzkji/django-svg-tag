"""Settings that need to be set in order to run the tests."""
import os
import logging


DEBUG = True

logging.getLogger("factory").setLevel(logging.WARN)

SITE_ID = 1
TIME_ZONE = 'Europe/Zurich'

APP_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), ".."))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sqlite.db',
    }
}

LANGUAGES = (
    ('en', 'EN', ),
)
LANGUAGE_CODE = 'en'

ROOT_URLCONF = 'test_app.urls'

# media root is overridden when needed in tests
MEDIA_ROOT = os.path.join(APP_ROOT, '../test_app_media')
MEDIA_URL = "/media/"
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(APP_ROOT, '../test_app_static')
STATICFILES_DIRS = (
    os.path.join(APP_ROOT, 'static'),
)

#TEMPLATE_DIRS = (
#    os.path.join(APP_ROOT, 'tests/test_app/templates'),
#)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                # 'django.template.loaders.eggs.Loader',
            ],
        }
    },
]

COVERAGE_REPORT_HTML_OUTPUT_DIR = os.path.join(
    os.path.join(APP_ROOT, 'tests/coverage'))
COVERAGE_MODULE_EXCLUDES = [
    'tests$', 'settings$', 'urls$', 'locale$',
    'migrations', 'fixtures', 'admin$', 'django_extensions',
]

EXTERNAL_APPS = (
    # 'django.contrib.admindocs',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
)

INTERNAL_APPS = (
    'test_app',
    'svg_tag',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

MIDDLEWARE = MIDDLEWARE_CLASSES

INSTALLED_APPS = EXTERNAL_APPS + INTERNAL_APPS
COVERAGE_MODULE_EXCLUDES += EXTERNAL_APPS

SECRET_KEY = 'foobarXXXxxsvXY'
