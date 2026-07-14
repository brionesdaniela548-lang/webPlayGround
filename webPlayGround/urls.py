from django.contrib import admin
from django.urls import path, include
from pages.urls import urlpatterns

urlpatterns = [
    path("", include('core.urls')),
    path("pages/", include(urlpatterns)),
    path("admin/", admin.site.urls),
    path("accounts/", include('registration.urls')),
]
