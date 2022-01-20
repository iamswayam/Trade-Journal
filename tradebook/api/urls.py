from django.contrib import admin
from django.urls import path
from tradebook.views import newnote
from .views import note_list, index_list, stock_list


urlpatterns = [
    path('list/', note_list, name="note-list"),
    path('indexapi/', index_list, name="index_list"),
    path('stockapi/', stock_list, name="stock_list"),
]
