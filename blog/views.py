from django.shortcuts import render
from django.http import HttpResponse
# HttpResponse is from django 


# function to return in a route 
def home(request):
    return HttpResponse('<h1>Blog Home</h1>')

# function to return in a route 

def about(request):
    return HttpResponse('<h1>Blog About</h1>')
