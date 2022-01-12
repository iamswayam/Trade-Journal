from django.contrib import admin
from django.urls import path
from tradebook.views import newnote
from .views import note_list


urlpatterns = [
    path('list/', note_list, name="note-list"),
    # path('<int:pk>', WatchDetailAV.as_view(), name='movie-detail'),
]
