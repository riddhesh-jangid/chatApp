# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from chat.models import user,message,allconnection
from django.urls import reverse
# Create your views here.

def login(request):
    return render(request,'chat/login.html')

def processdata(request):
    username = request.POST['username']
    password = request.POST['password']
    request.session['username'] = username
    loginorsingup = request.POST['choice']
    if loginorsingup=='login':
        accounts = user.objects.all()
        for account in accounts:
            if (account.username == username and account.password == password):
                request.session['token'] = account.token
                return HttpResponseRedirect('../show')
        return render(request,'chat/login.html',{'error_message':'Wrong username/password'})


    else:
        object = user(username,password)
        object.save()
        return HttpResponse("Sing up")


def show(request):
    try:
        username = request.session['username']
        token = request.session['token']
    except:
        return HttpResponseRedirect('../login')
    allaccount = user.objects.all()
    connections = allconnection.objects.all()
    return render(request,'chat/show.html',{'username':username,'token':token,'allaccount':allaccount,'connections':connections})

def logout(request):
    request.session.flush()
    return HttpResponseRedirect('../login')

def messages(request,user_id1,user_id2):
        if (request.POST):
            smessage = request.POST['sentmessage']
            alluser = user.objects.get(token=user_id1)
            object = message(token=alluser,text=smessage,rtoken=user_id2)
            object.save()
            checkconnections = allconnection.objects.all()
            count=0
            for x in checkconnections:
                if (int(user_id1)==x.token.token and int(user_id2)==x.ctoken):
                    count+=1
            if count==0:
                connectionobject = allconnection(token=alluser,ctoken=user_id2)
                connectionobject.save()
            alluser2 = user.objects.get(token=user_id2)
            count=0
            for x in checkconnections:
                if (int(user_id2)==x.token.token and int(user_id1)==x.ctoken):
                    count+=1
            if count==0:
                connectionobject = allconnection(token=alluser2,ctoken=user_id1)
                connectionobject.save()
        allmessage = message.objects.all()
        connections = allconnection.objects.all()
        user_id1 = int(user_id1)
        user_id2 = int(user_id2)
        username = user.objects.get(token=user_id2).username
        return render(request,'chat/message.html',{'user_id1':user_id1,'allmessage':allmessage,'user_id2':user_id2,'user':user,'username':username})
