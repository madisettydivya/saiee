from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app1_function(request):
    return HttpResponse('<h1>This is an app1_function</h1>') 
