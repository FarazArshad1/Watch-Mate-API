from django.urls import path,include
from . import views

urlpatterns = [
    path(route='list/',view=views.WatchListAV().as_view(),name = 'movies list'),
    path(route='<int:pk>/', view=views.WatchDetailAV().as_view(), name= 'movie Details'),
    path(route='stream/', view=views.StreamPlatformAV().as_view(), name='stream'),
    path(route= 'stream/<int:pk>/',view=views.PlatformDetailAV().as_view(), name='Platform Detail')
]