from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from Site import settings
from . import views

urlpatterns = [
    path('', views.main, name="main"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
