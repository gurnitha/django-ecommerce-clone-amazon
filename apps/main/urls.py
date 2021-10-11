# apps/main/urls.py

# Django modules
from django.urls import path

# Locals
from apps.main.views import homePage

# Appname
app_name='main'

# Urlpatterns
urlpatterns = [
    path('', homePage, name='homePage'),
]