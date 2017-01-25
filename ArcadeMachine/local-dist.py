# DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'arcademachine',
        'USER': 'arcademachine',
        'PASSWORD': '',
        'HOST': '',
        'PORT': 3306,
    },
}

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_STORAGE_BUCKET_NAME = 'arcademachine-images'
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_FILE_OVERWRITE = False
