from django import forms
import re
from django.core import validators

def password_check(value):
    if len(value) >20:
        raise forms.ValidationError('password max limit 10 characters')
    elif len(value) < 8:
        raise forms.ValidationError('password min limit 8 characters')
    elif value.isdigit():
        raise forms.ValidationError('all are digits')
    elif value.isalpha():
        raise forms.ValidationError('all are characters')
    elif value.isalnum():
        raise forms.ValidationError('please enter special characters')
    elif value.islower():
        raise forms.ValidationError('provide atleast one upper case characters')
    elif value.isupper():
        raise forms.ValidationError('please provide atleast one lowercase characters')
    return value

class Registration_Form(forms.Form):
    STATUS_TYPE = ((0,'user'),(1,'manager'))
    First_name=forms.CharField()
    Last_name=forms.CharField()
    Email_id = forms.EmailField()
    Phone_number = forms.IntegerField()
    Password = forms.CharField(validators=[password_check,])
    Conform_password = forms.CharField()
    Gender = forms.CharField()
    Age = forms.IntegerField()
    Date_of_birth = forms.DateField()
    Status = forms.IntegerField()
    Qualification = forms.CharField()

    def clean_Phone_number(self):
        phone_no = str(self.cleaned_data['Phone_number'])
        regex = re.compile(r"^(6|7|8|9)\d{9}$")
        if len(phone_no) == 10:
            match = regex.search(phone_no)
            if match:
                return phone_no
            raise forms.ValidationError('phone number must be 6|7|8|9')
        raise forms.ValidationError('Please enter 10 digits')

    def clean_Age(self):
        a = self.cleaned_data['Age']
        if a > 60:
            raise forms.ValidationError('age must be less than 60')
        elif a < 15:
            raise forms.ValidationError('age must be greater than 15')
        return a

    def clean_Conform_password(self):
        p = self.cleaned_data.get('Password')
        cp = self.cleaned_data.get('Conform_password')
        if p != cp:
            raise forms.ValidationError('password not matched')
        return cp
