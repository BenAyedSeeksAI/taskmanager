from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def main(request):
    return render(request, 'task/index.html')
    #return HttpResponse("<h1>Hello World</h1>")
def About_website(request):
    return render(request, 'task/about.html')