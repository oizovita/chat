import json

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import NameChat
from .forms import CreatChat
from django.contrib.auth.models import User


def room(request, room_name):
    users = User.objects.all()

    chats = NameChat.objects.all()
    l = []
    for c in chats:
        if str(c.user) == str(request.user):
            l.append(c.chat_name)

    if request.method == "POST":
        form = CreatChat(request.POST)
        if form.is_valid:
            id = form.data.getlist('check')
            for i in id:
                n = NameChat(user=User.objects.get(id=i), chat_name=form.data['chat_name'])
                n.save()
            return HttpResponseRedirect('/chat/createchat/' + form.data['chat_name'])
    else:
        form = CreatChat()

    return render(request, 'chat/room.html', {'room_name_json': mark_safe(json.dumps(room_name)), "form": form,
                                              'users': users, 'chats': l})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print(username)
            raw_password = form.cleaned_data.get('password1')
            print(raw_password)
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
