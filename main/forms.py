from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=120, required=True)
    phone = forms.CharField(max_length=20, required=True)
    #created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        model = Contact
        # fields = '__all__'
        exclude = ('created', )# and delete this
        #verbose_name_plural = 'Contact Profiles'
        #verbose_name = 'Contact Profile'
        
        
'''
widgets = {
'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'})
}
'''