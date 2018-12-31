from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Grazie di esistere Patricia!. Te iubesc :)")
