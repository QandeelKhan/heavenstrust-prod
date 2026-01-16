from .common import *


# Static files (CSS, JavaScript, Images)
# overriding the media url in production
MEDIA_URL = f'/space-heavenstrust/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'space-heavenstrust', 'media')

STATIC_URL = '/space-heavenstrust/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'space-heavenstrust', 'static')

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'assets'),
# ]
