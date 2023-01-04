from django.http import HttpResponse

# Hello world API
def index(request):
    return HttpResponse("Hello World!")