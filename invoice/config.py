import os

DEBUG = True
ENV = "development"
CSRF_ENABLED = True

SECRET_KEY = os.environ.get('SECRET_KEY') or '4d6f45a5fca12445dbac2f59c3b6c7cb1'

DATABASES = {
    'NAME': "invoice_local",
    'USER': "trellis",
    'PASSWORD': "Trellis123",
    'HOST': "localhost",
    'PORT': 5432
}

DATABASE_URL =  'postgresql://%(USER)s:%(PASSWORD)s@%(HOST)s:%(PORT)s/%(NAME)s' % DATABASES
