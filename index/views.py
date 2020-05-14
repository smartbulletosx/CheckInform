from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("<h3>Привет, Django</h3>")

