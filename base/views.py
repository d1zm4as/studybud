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


def room(request):
    return render(request, 'room.html')
