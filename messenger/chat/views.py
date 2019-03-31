import json
import os
import random
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import NameChat
from .models import UserColor
from .forms import CreatChat
from django.contrib.auth.models import User


# Checks if the folder already exists
# and if not then creates it
def create_folder(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except PermissionError:
        print("Path not found")
        exit()


create_folder('log')


def r(): return random.randint(0, 255)


def room(request, room_name):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/login/")

    u = User.objects.get(username=request.user.username)
    u.usercolor.color = '#%02X%02X%02X' % (r(), r(), r())
    u.usercolor.save()

    users = User.objects.all()
    chats = NameChat.objects.all()
    user_chats = []

    for chat in chats:
        if str(chat.user) == str(request.user):
            user_chats.append(chat.chat_name)

    if request.method == "POST":
        form = CreatChat(request.POST)
        if form.is_valid:
            id = form.data.getlist('check')
            for i in id:
                n = NameChat(user=User.objects.get(id=i),
                             chat_name=form.data['chat_name'])
                n.save()
            return HttpResponseRedirect('/chat/' + form.data['chat_name'])
    else:
        form = CreatChat()

    return render(request, 'chat/room.html', {'room_name_json': mark_safe(json.dumps(room_name)), "form": form,
                                              'users': users, 'chats': user_chats})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            UserColor.objects.create(color='#%02X%02X%02X' %
                                     (r(), r(), r()), user=user)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
