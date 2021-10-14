import os
import dj_database_url
from .base import *

SECRET_KEY = os.environ.get('SECRET_KEY', 'your-default-secret-key')

DEBUG = True
ALLOWED_HOSTS = ['topvineyards.herokuapp.com']


INSTALLED_APPS += [
    'cloudinary',
    'cloudinary_storage',
]


db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)


# Cloudinary config
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUD_NAME'),
    'API_KEY': os.environ.get('CLOUD_API_KEY'),
    'API_SECRET': os.environ.get('CLOUD_API_SECRET')
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


CORS_REPLACE_HTTPS_REFERER = True
HOST_SCHEME = "https://"
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_SECONDS = 1000000
SECURE_FRAME_DENY = True
