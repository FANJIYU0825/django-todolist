from django.shortcuts import render
from django.http import HttpResponse
from .models import visiterItem




def visiter_see(request):
    all_visiterItems = visiterItem.objects.all()
    return render(request,'visiter.html',{'all_items':all_visiterItems})