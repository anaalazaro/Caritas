"""
Django settings for Caritas project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h=pg&y22=9!d_(-qynef^$kn-l!p#xzfpog&a&ics34z1g=qw2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR/"static",
    os.path.join(BASE_DIR, 'app/static'),
    os.path.join(BASE_DIR, 'cargarArticulo/static'),
    os.path.join(BASE_DIR, 'Caritas/static'),

]


ALLOWED_HOSTS = []
CRISPY_TEMPLATE_PACK = 'bootstrap5'
CRISPY_ALLOWED_TEMPLATE_PACKS= "bootstrap5"

# Configuración de e-mail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 25  # or your SMTP port
EMAIL_USE_TLS = True  # or False if not using TLS
EMAIL_HOST_USER = 'ingecaritas@gmail.com'
EMAIL_HOST_PASSWORD = 'oicu xfuw xmvd valg'

# Application definition

INSTALLED_APPS = [
    'crispy_forms',
    'crispy_bootstrap5',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app', 'cargarArticulo',
    'verArticulosPendientes', 'controlarPublicacion',
    'verPerfilPropio',
    'autenticacionIntercambiador',
    'ayudanteAuth',
    'chngPassRequest',
    'changePassword',
    'registrarAyudante',
    'editarPerfilAdministrador',
    'verOtroUsuario',
    'eliminarCuenta',
    'verDetalleDeArticulo',
    'verAyudantesRegistrados',
    'verArticulosPropios',
    'buscarArticulo',
    'notificaciones'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Caritas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'app', 'templates'),
            os.path.join(BASE_DIR, 'autenticacionIntercambiador', 'templates'),
            os.path.join(BASE_DIR, 'Caritas', 'templates'),
            os.path.join(BASE_DIR, 'cargarArticulo', 'templates'),
            os.path.join(BASE_DIR, 'verPerfilPropio', 'templates'),
            os.path.join(BASE_DIR, 'verDetalleDeArticulo', 'templates'), os.path.join(BASE_DIR, 'verOtroUsuario', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'notificaciones.context_processors.notifications_processor'
            ],
        },
    },
]

WSGI_APPLICATION = 'Caritas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_USER_MODEL = 'app.CustomUser'
# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,  # Cambiar a 6 caracteres
        }
    }
]

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'
# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
# settings.py

LANGUAGE_CODE = 'es-es'

LANGUAGES = [
    ('es', 'Spanish'),
]
TIME_ZONE = 'UTC'  # Opcional, según tu zona horaria

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGOUT_REDIRECT_URL = 'inicio'

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'