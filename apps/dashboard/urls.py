# apps/dashboard/urls.py

# Django modules
from django.urls import path

# Locals
from apps.dashboard.views import homePage, categoriesPage

# appname
app_name = 'dashboard'

# Urlpatternts
urlpatterns = [

    # Path for dashboar app
    path('dashboard/', homePage, name='homePage'),
    path('dashboard/categories/', categoriesPage, name='categoriesPage'),
    
]

