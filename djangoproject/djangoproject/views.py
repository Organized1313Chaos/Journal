from django.http import HttpResponse

# Hello world API
def index(request):
    
    #HttpResponse can return A String, HTML content as well
    return HttpResponse("<h1>Hello World!<h1>")