from django.shortcuts import render
from django.http import HttpResponse,HttpResponsePermanentRedirect
from .models import visiterItem




def visiter_see(request):
    all_visiterItems = visiterItem.objects.all()
    return render(request,'visiter.html',{'all_items':all_visiterItems})


def addvisiter (request):
    new_item = visiterItem (content = request.POST['content'])
    new_item.save()
    return HttpResponsePermanentRedirect('/visiter/')

def deletevisiter (request,todo_id):
    item_delete = visiterItem.objects.get(id = todo_id)
    item_delete.delete()
    return HttpResponsePermanentRedirect('/visiter/')
