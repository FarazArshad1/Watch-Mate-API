from django.urls import path,include
from . import views

urlpatterns = [
    path(route='list/',view=views.MovieListAV.as_view(),name = 'movies list'),
    path(route='<int:pk>/', view=views.MovieDetailAV.as_view(), name= 'movie Details')
]