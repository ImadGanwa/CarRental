from Rental.models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class createUserForm(UserCreationForm):
    password1 = forms.CharField(
        # label="Password",
        widget=forms.PasswordInput(
            attrs={'class': 'input100', 'type': 'password', 'align': 'center'}),
    )
    password2 = forms.CharField(
        # label="Confirm password",
        widget=forms.PasswordInput(
            attrs={'class': 'input100', 'type': 'password', 'align': 'center'}),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input100'}),
            'email': forms.TextInput(attrs={'class': 'input100'}),
        }

class DateInput(forms.DateInput):
    input_type = 'date'

class completeUserForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ['cin', 'tel', 'dateN']
        widgets = {
            'cin' : forms.TextInput(attrs={'class': 'form-control p-4', 'placeholder': 'CIN', 'required': 'required'}),
            'tel': forms.TextInput(attrs={'class': 'form-control p-4', 'placeholder': 'Phone Number', 'required': 'required'}),
            'dateN': forms.DateInput(attrs={'class': 'form-control p-4 datetimepicker-input', 'type': 'date', 'placeholder': 'Birth Date', 'required': 'required'})
        }

class reservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['dateD', 'dateF']
        widgets = {
            'dateD': forms.DateInput(attrs={'class': 'form-control p-4 datetimepicker-input', 'type': 'date', 'placeholder': 'PickUp date', 'required': 'required'}),
            'dateF': forms.DateInput(attrs={'class': 'form-control p-4 datetimepicker-input', 'type': 'date', 'placeholder': 'DropOff date', 'required': 'required'})
        }

