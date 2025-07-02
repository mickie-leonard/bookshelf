from django.shortcuts import render

import re
from django.utils.timezone import datetime
from django.http import HttpResponse

def hello_there(request, name):
    print(request.build_absolute_uri()) #optional
    return render(
        request,
        'bookshelf_app/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
# Replace the existing home function with the one below
def home(request):
    return render(request, "bookshelf_app/home.html")

def about(request):
    return render(request, "bookshelf_app/about.html")

def contact(request):
    return render(request, "bookshelf_app/contact.html")



