from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def say_hello(request):
#     """
#     This is a 'View' function that can do anything you want
#     it to do as long as it's properly defined. For example,
#     you can write a function to
#     * Pull data from db
#     * Transform
#     * Send email response
#     For now we will get it to just say "Hello".
#     """
#     return HttpResponse('Hello World')

def calculate():
    x = 1
    y = 2
    return x

def say_hello(request):
    x = calculate()
    return render(request=request, template_name='hello.html', context={'name':'Nicholas'})
    
    