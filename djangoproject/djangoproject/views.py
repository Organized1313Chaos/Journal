from django.http import HttpResponse
from django.shortcuts import render
import re

# Hello world API
def index(request):
    google = r"https://google.com"
    leetcode = r"https://leetcode.com/"
   
    params = {'google': google, 'leetcode': leetcode}
    #render returns a template and context dictionary
    return render(request, 'index.html', params)

def analyze(request):
    text = request.POST.get('text', 'default')
    punctuation = request.POST.get('punctuation', 'off')
    
    if punctuation=='on':
        text = re.sub(r'[^\w\s]', '',  text)
        return HttpResponse(f"{text}")
    
    return HttpResponse('Error')