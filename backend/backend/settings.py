import os

from pathlib import Path
from backend.files.basic import *
from backend.files.development import *
from backend.files.graphql import *

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get('BOILERPLATE_SECRET_KEY', 'fallback')

DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}