from django import forms
from django.contrib.auth.models import User
from .models import NameChat


# Form for registration
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)


# Form for create chat
class CreatChat(forms.ModelForm):
    class Meta:
        model = NameChat
        widgets = {
            'chat_name': forms.TextInput(attrs={'placeholder': 'Enter new chat name'}),
        }
        fields = ('chat_name',)

    check = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=User.objects.all())
