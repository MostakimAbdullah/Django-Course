from django import forms
from django.core import validators


class contactForm(forms.Form):
    name=forms.CharField(label='User Name',help_text='You must need to provide a user name')
    file=forms.FileField(label='Image File')

def passmatch(value):
    if '#' and '@' not in value:
        raise forms.ValidationError('Your password must contain at least one special character (#, @)')


class StudentData(forms.Form):
    name=forms.CharField(required=False , help_text='Name of the student',validators=[validators.MaxLengthValidator(10,message='Please enter at least 10 characters')])
    password=forms.CharField( help_text='Type your password',widget=forms.PasswordInput,validators=[passmatch])
    


class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password=forms.CharField(label='Confirm Password', widget=forms.PasswordInput)


    def clean(self):
        cleaned_data=super().clean()
        password=self.cleaned_data['password']
        repassword=self.cleaned_data['confirm_password']
        if password!=repassword:
            raise forms.ValidationError('Passwords do not match')