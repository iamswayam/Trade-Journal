from django.contrib import admin
from django.urls import path
from django.urls import include
from tradebook.views import newnote


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tradebook.urls')),
    path('newnote/', newnote, name="newnote"),
]
