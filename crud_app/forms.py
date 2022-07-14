from django import forms
from .models import Detail , Blog
from django.forms.widgets import TextInput,EmailInput,NumberInput,Textarea

class DateInput(forms.DateInput):
    input_type = "date"

class Detail_form(forms.ModelForm):
    class Meta:
        model = Detail
        fields = "__all__"

        widgets = {
            'name' : TextInput(attrs={'placeholder' : 'Enter Your Name'}),
            'email' : EmailInput(attrs={'placeholder' : 'Enter Your Email address'}),
            'phone' : NumberInput(attrs={'placeholder' : 'Enter Your Phone Number'}),
            'address': TextInput(attrs={'placeholder': 'Enter Your Address'}),
            'dob': DateInput(),
        }

class Blog_form(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"

        widgets = {
            'title' : TextInput(attrs={'placeholder' : 'Enter Your Title'}),
            'desc' : Textarea(attrs={'placeholder' : 'Descripion'}),
            'upload_by': TextInput(attrs={'placeholder': 'Enter Your Name'}),
        }