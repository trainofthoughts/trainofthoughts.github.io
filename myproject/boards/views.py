from django.shortcuts import render

"""
Views are Python functions that receive an HttpRequest object and returns an 
HttpResponse object. 
Receive a request as a parameter and returns a response as a result.
"""
# Create your views here.
from django.http import HttpResponse
def home(request):
    return HttpResponse('test test test')
    