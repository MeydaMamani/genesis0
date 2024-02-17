from .base import *

DEBUG = True

ALLOWED_HOSTS = []

# DATABASES = {
#     'default': {
#         'ENGINE': 'mssql',
#         'NAME': 'BD_PRUEBA',
#         'USER': 'meyda',
#         'PASSWORD': 'meyda123$',
#         'HOST': '127.0.0.1',
#         'PORT': '1439',
#         'OPTIONS': {
#             'driver': 'ODBC Driver 17 for SQL Server',
#         },
#     }
# }

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DATABASE_CONNECTION_POOLING = False

STATIC_URL = '/static/'