from django.http import HttpResponse
from django.shortcuts import render
def nope(req):
    return HttpResponse("yaay!")
def okay(req):
    return HttpResponse("This is another name")
def text(req):
    return HttpResponse("<h1>This is the landing page</h1>")
def average(req):
    return HttpResponse("<p>Hello World Is Cliche</p>")
def index(req):
    return render(req,"index1.html")