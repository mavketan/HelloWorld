from django.shortcuts import render, render_to_response
from models import Line

# Create your views here.
from django.http import HttpResponse
def foo(request):
    return HttpResponse("Hello World!")


def foo1(request):
    name = "Ketan"
    html = "<html><body>Hello World! from %s</body></html>" % name
    return HttpResponse(html)

def foo2(request):
    return render_to_response("helloDJ/home.html",
				{"Testing" : "Django Template Inheritance ",
				"HelloHello" : "Hello World - Django"})

def foo3(request):
    return render_to_response("helloDJ/home2.html",
				{"lines" : Line.objects.all()})
