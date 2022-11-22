from django.shortcuts import render, redirect

# Create your views here.
from .models import Contact


def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        query = request.POST.get('query')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.query = query
        contact.save()
        return redirect("customers/")
    else:
        return render(request, 'contact.html')


def disp_cust(request):
    all_cust_details = Contact.objects.all()
    print(all_cust_details)
    context = {
        'allstu': all_cust_details
    }

    return render(request, 'display.html', context)
