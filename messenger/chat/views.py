import json
import os
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import NameChat
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


def room(request, room_name):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/login/")

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
                n = NameChat(user=User.objects.get(id=i), chat_name=form.data['chat_name'])
                n.save()
            return HttpResponseRedirect('/chat/' + form.data['chat_name'])
    else:
        form = CreatChat()

    return render(request, 'chat/room.html', {'room_name_json': mark_safe(json.dumps(room_name)), "form": form,
                                              'users': users, 'chats': user_chats})


def delete(request, user, chat_name):
    try:
        person = NameChat.objects.get(user=user, chat_name=chat_name)
        person.delete()
        return HttpResponseRedirect("chat/global")
    except NameChat.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")



def register(request):
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
