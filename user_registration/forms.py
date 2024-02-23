from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'job_title']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if any(char.isdigit() for char in name):
            raise forms.ValidationError("Name cannot contain numbers.")
        if len(name) < 4:
            raise forms.ValidationError("Name should be at least 4 characters long.")
        return name

    def clean_job_title(self):
        job_title = self.cleaned_data.get('job_title')
        if any(char.isdigit() for char in job_title):
            raise forms.ValidationError("Job title cannot contain numbers.")
        if len(job_title) < 14:
            raise forms.ValidationError("Job title should be at least 14 characters long.")
        return job_title

class LoginForm(forms.Form):
    email = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())