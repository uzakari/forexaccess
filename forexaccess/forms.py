from django.forms import ModelForm, TextInput, Textarea, Select, PasswordInput,EmailField, ChoiceField, CheckboxSelectMultiple
from .models import ContactUs
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class ContactForm(ModelForm):

    class Meta:
        model = ContactUs
        fields = ['reason', 'First_name', 'Last_name', 'Email', 'phone_number', 'subject', 'request']
        widgets = {'reason': Select(attrs={'class': 'form-control form-control-lg'}),
                   'First_name': TextInput(attrs={'class': 'form-control form-control-lg ', 'placeholder':'First Name'}),
                    'Last_name': TextInput(attrs={'class': 'form-control form-control-lg ', 'placeholder':' Last Name'}),
                    'Email': TextInput(attrs={'class': 'form-control form-control-lg ', 'placeholder': 'Email Address'}),
                   'phone_number': TextInput(attrs={'class': 'form-control form-control-lg ', 'placeholder': 'Phone Number'}),
                   'subject': TextInput(attrs={'class': 'form-control form-control-lg ', 'placeholder': 'Subject'}),
                   'request': Textarea(attrs={'class': 'form-control form-control-lg ', 'placeholder': 'Request',
                                              'cols': '20', 'rows': '5'})
                   }


# class UserReg(UserCreationForm):
#     email = forms.EmailField(required=True)
#
#     class Meta:
#         model = User
#         fields = {
#             'username', 'first_name', 'last_name', 'email',
#             'password', 'password2'
#         }
#
#     def save(self, commit=True):
#         user = super(UserReg, self).save(commit=False)


class RegisterationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(RegisterationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user