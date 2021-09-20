import dj_database_url
from .base import *

DEBUG = False
ALLOWED_HOSTS = ['topvineyards.herokuapp.com']

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
