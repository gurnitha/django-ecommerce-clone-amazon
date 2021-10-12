# config/urls.py

# Django modules
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # Path for main app
    path('', include('apps.main.urls', namespace='main')),

    # Path for dashboard app
    path('', include('apps.dashboard.urls', namespace='dashboard')),

    # Path for admin app
    path('admin/', admin.site.urls),
] +static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
