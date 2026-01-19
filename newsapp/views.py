from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloViews(request):
    return HttpResponse("Hello dars")