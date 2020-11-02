from pathlib import Path
from backend.files.basic import *
from backend.files.development import *
from backend.files.graphql import *

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = '2lj$9uu7bg96z!02c_%4-z^9ad6)w(1y$@mixlp^!ea+-0%e(6'

DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}