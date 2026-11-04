"""
Configuración del proyecto Fundación Patrimonio Vivo.
"""
import os
from pathlib import Path



# Carpeta raíz del proyecto (la que contiene manage.py)
BASE_DIR = Path(__file__).resolve().parent.parent

# Clave de desarrollo. En un sistema real iría en una variable de entorno.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'clave-solo-para-desarrollo')

DEBUG = True

ALLOWED_HOSTS = []


# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'catalogo',  # nuestra aplicación
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

ROOT_URLCONF = 'patrimonio_vivo.urls'

# Los templates están en la carpeta "templates" de la raíz del proyecto
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',  # da acceso a "user" y "perms"
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'patrimonio_vivo.wsgi.application'


# Base de datos (SQLite, no requiere instalar nada más)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Idioma y zona horaria
LANGUAGE_CODE = 'es-cl'
TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_TZ = True


# Archivos estáticos (CSS) que viven en la carpeta "static" de la raíz
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Autenticación
LOGIN_URL = 'login'              # a dónde se manda a quien no ha iniciado sesión
LOGIN_REDIRECT_URL = 'gestion'   # a dónde va después de iniciar sesión
LOGOUT_REDIRECT_URL = 'inicio'   # a dónde va después de cerrar sesión
