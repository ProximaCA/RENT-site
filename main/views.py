from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, r"html/index.html")

# def index(request):
    # return HttpResponseRedirect('http://example.com/')
def about(request):
    return render(request, r"html/about.html")