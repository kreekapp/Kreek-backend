"""
Django settings for currency_backend project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, PKCS1_v1_5
from base64 import b64decode, b16decode

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d7opbi5h3j5hyig378q&z!mi$m^mo%u)wog*8w%^wd=60@o*xk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'corsheaders',
    'django.contrib.staticfiles',
    'sslserver',
    'djangosecure',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'xMiddleware.logger.RequestLogMiddleware',
]

ROOT_URLCONF = 'currency_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'currency_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440000  #上传文件大小，改成25M
DATA_UPLOAD_MAX_MEMORY_SIZE = 2621440000  #上传数据大小，也改成了25M
# 为了防止cookie被阻止，这里要设置这两行，因为新的浏览器设置
# 开发环境设置这两行，生产环境注释这两行！
SESSION_COOKIE_SAMESITE = 'none'
CSRF_COOKIE_SAMESITE = 'none'
# 以下两行为是否为https链接，在标准配置中，如果前后台地址不同，则设置跨域必须加上这行
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = False # 将所有非SSL请求永久重定向到SSL
# SESSION_COOKIE_SECURE = False # 仅通过https传输cookie
# CSRF_COOKIE_SECURE = False # 仅通过https传输cookie
# SECURE_HSTS_INCLUDE_SUBDOMAINS = False # 严格要求使用https协议传输
# SECURE_HSTS_PRELOAD = False # HSTS为
# SECURE_HSTS_SECONDS = 60
# SECURE_CONTENT_TYPE_NOSNIFF = False # 防止浏览器猜测资产的内容类型
# SESSION_COOKIE_AGE = 1209600             # Session的cookie失效日期（2周）（数字为秒数）（默认）
# SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # 是否关闭浏览器使得Session过期（默认）


CORS_ORIGIN_WHITELIST = ()
 
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)
 
CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)

# RSA_PRIVATE_KEY = RSA.import_key(open('rsa_1024_priv.pem').read())
# # 实例化加密套件
# CIPHER = PKCS1_v1_5.new(RSA_PRIVATE_KEY)

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://localhost:6379',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
             "PASSWORD": "Qw123456789",
        },
    },
}
REDIS_TIMEOUT=7*24*60*60
CUBES_REDIS_TIMEOUT=60*60
NEVER_REDIS_TIMEOUT=365*24*60*60

# 日志信息
LOGGING = {
    # 版本
    'version': 1,
    # 是否禁止默认配置的记录器
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '{"time": "%(asctime)s", "level": "%(levelname)s", "method": "%(method)s", "username": "%(username)s", "role": "%(role)s","sip": "%(sip)s", "dip": "%(dip)s", "path": "%(path)s", "status_code": "%(status_code)s", "reason_phrase": "%(reason_phrase)s", "func": "%(module)s.%(funcName)s:%(lineno)d",  "message": "%(message)s", "body": "%(body)s","response":"%(response)s"}',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    # 过滤器
    'filters': {
        'request_info': {'()': 'xMiddleware.logger.RequestLogFilter'},
    },
    'handlers': {
        # 标准输出
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
        # 自定义 handlers，输出到文件
        'restful_api': {
            'level': 'DEBUG',
            # 时间滚动切分
            'class': 'logging.StreamHandler',
            # 'filename': os.path.join(os.getcwd(), 'logs/web-log.log'),
            # 'formatter': 'standard',
            # # 调用过滤器
            # 'filters': ['request_info'],
            # # 每天凌晨切分
            # 'when': 'MIDNIGHT',
            # # 保存 30 天
            # 'backupCount': 30,
        },
    },
    'loggers': {
        # 'django': {
        #     'handlers': ['console'],
        #     'level': 'INFO', #
        #     'propagate': False
        # },
        'web.log': {
            'handlers': ['restful_api'],
            'level': 'INFO',
            # 此记录器处理过的消息就不再让 django 记录器再次处理了
            'propagate': False
        },
    }
}