from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from pele import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('appointment.urls', namespace='appointment')),
]

urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
