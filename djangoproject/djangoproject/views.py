from django.http import HttpResponse
from django.shortcuts import render

# Hello world API
def index(request):
    
    #HttpResponse can return A String, HTML content as well
    return render(request, 'index.html')