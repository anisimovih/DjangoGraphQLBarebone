"""Environment settings. Probably for any environment except tests."""
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'default_local_key')