from django.contrib import admin
from django.urls import path, include
from tradebook.views import newnote


urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('secret/', admin.site.urls),
    path('', include('tradebook.urls')),
    path('newnote/', newnote, name="newnote"),
    path('api/', include('tradebook.api.urls')),
]
