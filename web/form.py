from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from .models import Record
from django.forms import ModelForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs= {'placeholder':'First name'}))

    last_name = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs= {'placeholder':'Last name'}))

    email = forms.EmailField(label="", widget=forms.TextInput(attrs= {'class': 'form-control', 'placeholder':'Email adress'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username' 
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="from-text text-muted small">'

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First name' 
        self.fields['first_name'].label = ''
        self.fields['first_name'].help_text = '<span class="from-text text-muted small">'

        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last name' 
        self.fields['last_name'].label = ''
        self.fields['last_name'].help_text = '<span class="from-text text-muted small">'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] =  'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<span class="from-text text-muted small"> <ul> <li> Your password can\'t be too similato your personal information.</li> <li> Your password must contain atleast 8 characters.</li> <li> Your password can\'t be a commonly used password.</li> <li> Your passowrd can\'t be entirely numeric. </li></ul> '

        self.fields['password2'].widget.attrs['class'] =  'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="from-text text-muted small">'
            
# Add record form
class AddRecord(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'First name', 'class': 'form-control'}))

    last_name = forms.CharField(max_length=50, required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Last name', 'class': 'form-control'}))

    email = forms.CharField(max_length=50, required=True, widget=forms.widgets.EmailInput(attrs={'placeholder': 'Email address', 'class': 'form-control'}))

    phone = forms.CharField(max_length=50, required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Phone number', 'class': 'form-control'}))

    address = forms.CharField(max_length=50, required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Address', 'class': 'form-control'}))

    city = forms.CharField(max_length=50, required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'City', 'class': 'form-control'}))

    state = forms.CharField(max_length=50, required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'State', 'class': 'form-control'}))

    zipcode = forms.CharField(max_length=50, required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Zipcode', 'class': 'form-control'}))

    class Meta:
        model = Record 
        exclude = ('User',)

