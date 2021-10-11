# apps/main/urls.py

# Django modules
from django.urls import path

# Locals
from apps.main.views import helloWorld

# Appname
app_name='main'

# Urlpatterns
urlpatterns = [
    path('', helloWorld),
]