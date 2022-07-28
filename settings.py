import django_heroku
Debug =  bool( os.environ.get('DJANGO_DEBUG', False) )
ALLOWED_HOSTS = ['*']
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware', #Добавляем до 'django.middleware.security.SecurityMiddleware',
]

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'email@gmail.com' #С которого будет приходить сообщение
EMAIL_HOST_PASSWORD = 'password'
EMAIL_PORT = 587

ADMINS = [
    ('Kat', 'katvilinskimazur@gmail.com'),
]
WHITENOISE_USE_FINDERS = True
STATIC_ROOT = None
django_heroku.settings(locals()) #В конце
