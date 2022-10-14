"""Default settings for any environment."""

from GraphQLBarebone.settings.default import *
from GraphQLBarebone.settings.environment import *

DEBUG = True

SHELL_PLUS_PRINT_SQL_TRUNCATE = 1000

print(BASE_DIR)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
