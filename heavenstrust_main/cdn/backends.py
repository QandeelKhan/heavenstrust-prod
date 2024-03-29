from django.conf import settings
from storages.backends.s3 import S3Storage 



class StaticStorage(S3Storage):
    bucket_name = 'heavenstrust-bucket'
    location = 'space-heavenstrust/static'



class MediaStorage(S3Storage):
    bucket_name = 'heavenstrust-bucket'
    location = 'space-heavenstrust/media'
    # default_acl = 'public-read'

# above provided locations we set similar to our local settings so the directories
# name and locations on the our hosted app on cloud look similar to our local file
# structure. we can type any name i.e "static-abc", "root-abcd".

# making settings for our static assets to after that set in conf.py
# this will make upload our static folder into digitalocean,
# this will make anything uploading through our models will go there in media folder on digitalocean.