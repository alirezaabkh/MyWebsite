from django import forms
from django.forms import ModelForm
from website.models import Contact

class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)


class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'