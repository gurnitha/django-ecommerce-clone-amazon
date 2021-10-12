# apps/dashboard/views.py

# Django modules
from django.shortcuts import render


# Create your views here.


# View method name:homePage
def homePage(request):
	return render(request, 'dashboard/home_page.html')