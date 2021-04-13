import environ

from tourist_attractions.settings.base import *

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
    DEFAULT_FILE_STORAGE='storages.backends.s3boto3.S3Boto3Storage'
)

# False if not in os.environ
DEBUG = env('DEBUG')
DEFAULT_FILE_STORAGE = env('DEFAULT_FILE_STORAGE')
# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

# Parse database connection url strings like psql://user:pass@127.0.0.1:8458/db
DATABASES = {
    # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found
    'default': env.db(),
}
