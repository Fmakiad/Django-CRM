from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms 


class SignUpFrom(UserChangeForm):
    first_name = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs= {'placeholder':'First name'}))

    last_name = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs= {'placeholder':'Last name'}))

    email = forms.EmailField(label="", widget=forms.TextInput(attrs= {'class': 'form-control', 'placeholder':'Email adress'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'password1')

    def __init__(self, *args, **kwargs):
        super(SignUpFrom, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attr['class'] = 'form-control'
        self.fields['username'].widget.attr['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = ''

        self.fields['password1'].widget.attr['class': 'form-control']
        self.fields['password1'].widget.attr['placeholder': 'password']
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<span class="from-text text-muted small"> <ul> <li> Your password can\'t be too similato your personal information.</li> <li> Your password must contain atleast 8 characters.</li> <li> Your password can\'t be commonly used password.</li> <li> Your passowrd can\'t be entirely numeric. </li></ul> '

        self.fields['password2'].widget.attr['class': 'form-control']
        self.fields['password2'].widget.attr['placeholder': 'password2']
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="from-text text-muted small"> <ul> <li> Your password can\'t be too similato your personal information.</li> <li> Your password must contain atleast 8 characters.</li> <li> Your password can\'t be commonly used password.</li> <li> Your passowrd can\'t be entirely numeric. </li></ul> '
            

