from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rental.urls')),
    path('users/', include('registration.backends.simple.urls')),
]