# config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # Path for main app
    path('', include('apps.main.urls', namespace='main')),

    # Path for dashboard app
    path('', include('apps.dashboard.urls', namespace='dashboard')),

    # Path for admin app
    path('admin/', admin.site.urls),
]
