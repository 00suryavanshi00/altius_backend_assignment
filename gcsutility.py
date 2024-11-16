

from storages.backends.gcloud import GoogleCloudStorage

Media = lambda: GoogleCloudStorage(location='media')

Static = lambda: GoogleCloudStorage(location='static')

# couldn't complete this due to lack of time but i've the bucket on public mode ready with all the required
# perms