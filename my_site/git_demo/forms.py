from django import forms
from django.contrib.auth.models import User
from git_demo.models import Person


class PersonForm(forms.ModelForm):
    age = forms.IntegerField(widget=forms.NumberInput)

    class Meta:
        model = Person
        fields = ('age',)

class UserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput)
    last_name = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',)