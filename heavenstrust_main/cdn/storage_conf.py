import os
from decouple import config
from heavenstrust_main.settings import BASE_DIR

USE_SPACES = config('USE_SPACES', cast=bool, default=True)
# USE_SPACES=False
if USE_SPACES:
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = "us-east-1"
    AWS_DEFAULT_ACL = None
    AWS_S3_FILE_OVERWRITE=None
    #
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static files settings
    # STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/space-lifesyncnow/static/'
    STATICFILES_STORAGE = 'heavenstrust_main.cdn.backends.StaticStorage'

    # Media files settings
    PUBLIC_MEDIA_LOCATION = 'space-heavenstrust/media'
    MEDIA_ROOT= "space-heavenstrust/media"
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'
    # MEDIA_URL = 'https://heavenstrust-bucket.s3.amazonaws.com/'
    DEFAULT_FILE_STORAGE = 'heavenstrust_main.cdn.backends.MediaStorage'
    #
    # Static files settings
    # STATIC_URL = "https://life-sync-now-bucket.s3.ap-south-1.amazonaws.com/space-lifesyncnow/static/"
    #
    # s3 static settings
    AWS_LOCATION = 'space-heavenstrust/static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
    # DEFAULT_FILE_STORAGE = 'storages.backends.s3.S3Storage'
else:
    STATIC_URL = '/space-heavenstrust/static/'
    # STATIC_ROOT = BASE_DIR / "space-heavenstrust/static"
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'space-heavenstrust/media'
STATICFILES_DIRS = (
    BASE_DIR / 'space-heavenstrust/static',
)
# helping material
# https://testdriven.io/blog/django-digitalocean-spaces/
# https://shopingly-space.fra1.digitaloceanspaces.com/media/productimg/0_98drx4MegZUq4iTd.jpeg
