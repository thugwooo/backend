from .base import *

DEBUG = False

INSTALLED_APPS += (
    #배포 환경에서 설치할 앱들
)
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'maindb',
        'USER': 'louis',
        'PASSWORD': 'louis',
        'HOST': 'ec2-3-128-190-192.us-east-2.compute.amazonaws.com',
        'PORT': '5432',
    }
}