from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Patricia este foarte frumoasa şi o iubesc!")
