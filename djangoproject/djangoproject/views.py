from django.http import HttpResponse
from django.shortcuts import render

# Hello world API
def index(request):
    
    #render returns a template and context dictionary
    return render(request, 'index.html')