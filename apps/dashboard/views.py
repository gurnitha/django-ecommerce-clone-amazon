# apps/dashboard/views.py

# Django modules
from django.shortcuts import render


# Create your views here.


# View method name:homePage
def homePage(request):
	return render(request, 'dashboard/index.html')


# View method name:categoriesPage
def categoriesPage(request):
	return render(request, 'dashboard/categories.html')