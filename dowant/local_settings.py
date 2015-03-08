# -*- coding: utf-8 -*-

ADMINS = (
  ('guestpub', 'pointer81@gmail.com'),
  )

EMAIL_HOST = 'smtp.cafe24.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587 
EMAIL_HOST_USER = 'hoodpub@hoodpub.com'
EMAIL_HOST_PASSWORD = 'hmchoi81' 
SERVER_EMAIL = 'pointer81@gmail.com'

DATABASES = {
    'default': {
    'ENGINE': 'django.contrib.gis.db.backends.postgis',
    'NAME': 'guestpub',
    'HOST': '127.0.0.1',
    'USER': 'guestpub',
    'PASSWORD': 'guestpub',
    'PORT': ''}
}

CONSTANCE_BACKEND = 'constance.backends.redisd.RedisBackend'
CONSTANCE_REDIS_CONNECTION = 'redis://localhost:6379/0'
CONSTANCE_CONFIG = {
    'ENABLE_SEND_SMS': (False, u'문자 전송 여부 설정,'
                        u'True: 전송가능, False: 전송불가'),
}

BLUEHOUSE_APPID = 'guestpub'
BLUEHOUSE_APIKEY = '8c1854a8635111e48910040113e09101'
BLUEHOUSE_URL = 'api.bluehouselab.com'
