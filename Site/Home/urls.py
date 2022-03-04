from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from Site import settings
from .views import MainView


urlpatterns = [
    path('', MainView.as_view(), name="Home_MainView"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
