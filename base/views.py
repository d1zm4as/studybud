from django.shortcuts import render
# Create your views here.
rooms  = [

    {'id':1, 'name':'Lets learn Python'},
    {'id':2, 'name':'Lets learn Chess'},
    {'id':3, 'name':'Lets learn Git'},

]






def home(request):
    context = {'rooms':rooms}
    return render(request,'base/home.html',context)


def room(request,pk):
    room = None

    for x in rooms:
        if x['id']==int(pk):
            room =x
    context  = {'room':room}
    return render(request, 'base/room.html',context)
