from .base import *


def read_secrets(secret_name):
    file = open('/run/secrets/' + secret_name)
    secret = file.readline().strip()
    file.close()
    return secret


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = read_secrets('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# mariadb 가 mysql 에서 분기되어 나온 DB
# 그래서 mysql driver 사용해서 mariadb 와 연결해도 문제 없음!!
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': read_secrets('MARIADB_USER'),
        'PASSWORD': read_secrets('MARIADB_PASSWORD'),
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}
