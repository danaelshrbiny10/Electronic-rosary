from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('islamic/', include('islamic.urls')),
    path('admin/', admin.site.urls),
]
