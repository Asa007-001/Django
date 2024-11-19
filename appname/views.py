from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def index(request):
    #return HttpResponse("me")
    return render(request,"index.html")
def me(request):
    #return HttpResponse("It's me")
    user={'name':'May','age':20,'place':'高雄'}
    return render(request,"It's me.html",user)
def you(request):
    #return HttpResponse("you")
    user={'name':'Sakura','age':18,'place':'高雄'}
    return render(request,"you.html",user)
def we(request):
    return render(request,"we.html")