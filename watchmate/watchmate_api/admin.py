from django.contrib import admin
from watchmate_api.models import WatchList, StreamPlatform

# Register your models here.
admin.site.register(WatchList)
admin.site.register(StreamPlatform)