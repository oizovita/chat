from django import forms
from django.contrib.auth.models import User
from .models import NameChat

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)


class CreatChat(forms.ModelForm):
    class Meta:
        model = NameChat

        fields = ('chat_name',)

    check = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=User.objects.all())
