from .base import *

env_list = dict()

local_env = open(os.path.join(BASE_DIR, '.env'))

while True:
    line = local_env.readline()
    if not line:
        break
    line = line.replace('\n', '')
    start = line.find('=')
    key = line[:start]
    value = line[start + 1:]
    env_list[key] = value

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env_list['SECRET_KEY']

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
        'USER': 'django',
        'PASSWORD': 'admin',
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}
