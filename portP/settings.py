"""
Django settings for portP project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y9u_84d!^y274fah@f@3d*5c4xr8b4c26567b2+w5y^u1o=d_%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*','.vercel.app','127.0.0.1']
# ALLOWED_HOST = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portapp'
]

WSGI_APPLICATION = 'portP.wsgi.application'
# WSGI_APPLICATION = 'portP.app.wsgi.app'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
     "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portP.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR , 'templates'],
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

# WSGI_APPLICATION = 'dams.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'mydbmydb',
#         'ENFORCE_SCHEMA': True,
#         'CLIENT':{
#             "host": "mongodb+srv://nsti:123@cluster0.tu9holz.mongodb.net/?retryWrites=true&w=majority",
#             "username" :'nsti',
#             "password" : '123',
#             "authMechanism" : 'SCRAM-SHA-1'
#         }

#     }
# }


# DATABASES = {
#     'default': {
#         'ENGINE': 'POSTGRESQL',
#         'NAME': 'portdb_nrrc',
#         'ENFORCE_SCHEMA': True,
#         'CLIENT':{
#             "host": "dpg-cjne1cmqdesc739hb7ug-a",
#             "username" :'shrey',
#             "password" : 'QVisCefMX1OZ0r7apZUS5AENe4yv7HKD',
#             "authMechanism" : 'SCRAM-SHA-1'
#         }

#     }
# }

import environ
env = environ.Env() # set default values and casting
environ.Env.read_env()

import dj_database_url
# # import env
DATABASES={
     'default' :  dj_database_url.parse('postgres://shrey:QVisCefMX1OZ0r7apZUS5AENe4yv7HKD@dpg-cjne1cmqdesc739hb7ug-a.singapore-postgres.render.com/portdb_nrrc')
            }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


# STAICFILES_DIRS = [BASE_DIR / 'static']
# STATIC_URL = 'static/'
STAICFILES_DIRS = [BASE_DIR / 'static']
STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"






























