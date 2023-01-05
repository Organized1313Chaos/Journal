from django.http import HttpResponse
from django.shortcuts import render

# Hello world API
def index(request):
    #render returns a template and context dictionary
    return render(request, 'index.html')

def removepunc(request):
    text = request.GET.get('text', 'default')
    return HttpResponse("removing punctuations..."+f"===========> {text}")