from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']  # সঠিক ফিল্ডগুলো

class EmailSearchForm(forms.Form):
    email = forms.EmailField(label='Enter your email')

class ReplyForm(forms.Form):
    reply = forms.CharField(widget=forms.Textarea, label='Reply')