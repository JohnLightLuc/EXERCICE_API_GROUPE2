from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import *

def polls_list(request):
    MAX_OBJECTS = 20
    polls = Categories.objects.all()[:MAX_OBJECTS]
    data = {"results": list(polls.values("nom", "description", "image","statut", "date_add","date_update" ))}
    return JsonResponse(data)


def polls_detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {"results": {
        "nom": poll.nom,
        "created_by": poll.created_by.username,
        "pub_date": poll.pub_date
    }}
    return JsonResponse(data)