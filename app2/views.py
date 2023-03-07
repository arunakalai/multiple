from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_app1(request):
    return HttpResponse('<marquee> this is first_app1</marquee>')
def second_app1(request):
    return HttpResponse('<h2> This is Seond_app1</h2>')
def first_app2(request):
    return HttpResponse('<h1> This is my first_app2</h2')
def second_app2(request):
    return HttpResponse('<marquee> This is my second_app2</marquee>')