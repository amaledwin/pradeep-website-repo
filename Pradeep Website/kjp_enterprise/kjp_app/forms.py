from django import forms
from kjp_app.models import AddClientsModel
from django.core import validators

def len_job_location(value):
    if len(value) < 2:
        raise forms.ValidationError("Must be more than one character")

def ph_num_isdig(value):
    if not(value.isdigit()):
        raise forms.ValidationError("Alphabets are not allowed")


class AddClientsForm(forms.ModelForm):
    client_job_location = forms.CharField(max_length=100,validators=[len_job_location,])
    client_phone_num = forms.CharField(max_length=100,validators=[validators.MaxLengthValidator(10),ph_num_isdig])

    class Meta():
        model = AddClientsModel
        fields = '__all__'
