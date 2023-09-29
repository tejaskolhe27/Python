from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, World')

def welcome(request):
    return HttpResponse('Welcome to Django!!!')

def html(request):
    html="""
    <h1 style="color:blue;">My First Heading</h1>
    <h2 style="color:red;">This is header 2</h2>
    <p>My first paragraph.</p>
    <button>Click me</button>

"""
    return HttpResponse(html)

def factorial(request):
    return HttpResponse("FACTORIAL")