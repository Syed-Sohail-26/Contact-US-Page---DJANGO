from django.apps import AppConfig
from django.shortcuts import render

class ContactAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contact_app'

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def disp_cust(request):
    return render(request, 'display.html')