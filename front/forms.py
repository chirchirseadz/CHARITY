from django import forms
from .models import Message, Gallary



class MessageEmailForm(forms.ModelForm):
    name= forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'placeholder':'Enter your name'}))
    subject= forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'placeholder':'Enter your  subject'}))
    email= forms.CharField(max_length=100,
                           widget= forms.EmailInput
                           (attrs={'placeholder':'Enter your email'}))
    body = forms.CharField(max_length=100,
                           widget= forms.Textarea
                           (attrs={'placeholder':'Give us your feed back'}))
    phone= forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'placeholder':'(xxx)xxx-xxxx'}))
    class Meta:
        model = Message
        fields = ['name','email','subject','body','phone']