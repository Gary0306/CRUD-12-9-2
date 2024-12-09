from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("index.urls")),
    path("products/", include("products.urls")),
]