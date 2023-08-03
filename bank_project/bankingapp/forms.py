from django import forms
from .models import District, SubDistrict

class PersonForm(forms.Form):
    name = forms.CharField(max_length=100)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    district = forms.ModelChoiceField(queryset=District.objects.all())
    sub_district = forms.ModelChoiceField(queryset=SubDistrict.objects.none())
    age = forms.IntegerField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    phone_number = forms.CharField(max_length=20)
    email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    ACCOUNT_TYPE_CHOICES = [
        ('Select','Select'),
        ('Savings', 'Savings'),
        ('Current', 'Current'),
        ('Fixed Deposit', 'Fixed Deposit'),
    ]
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPE_CHOICES)
    materials_provided = forms.MultipleChoiceField(
        choices=[
            ('Debit card', 'Debit card'),
            ('Credit card', 'Credit card'),
            ('Cheque book', 'Cheque book'),
        ],
        widget=forms.CheckboxSelectMultiple,
    )

