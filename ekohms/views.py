from django.shortcuts import get_object_or_404, render
from .models import *
# from django.http import HttpResponse


# Create your views here.

room_types = RoomType.objects.all()
context = {'rooms': room_types}


def index(request):
    return render(request, 'ekohms/index.html', context)


def rooms(request):
    return render(request, 'ekohms/rooms.html', context)


def contact(request):
    return render(request, 'ekohms/contact.html')


def about(request):
    context = {'title': 'About',
               'info': 'A fairy tale where your wishes come true'}
    return render(request, 'ekohms/about.html', context)


def rooms_detailed_view(request, room_id):
    room_detail = get_object_or_404(RoomType, pk=room_id)
    return render(request, 'ekohms/rooms_views.html',{'room': room_detail,'rooms': room_types})
