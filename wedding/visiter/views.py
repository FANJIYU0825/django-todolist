from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def visiter_see(request):

    return render(request,'visiter.html')