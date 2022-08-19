from django.contrib.auth.forms import User
from django.forms import ModelForm
from .models import *

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        
class ContactForm(ModelForm):
    class Meta:
        model = Contactus
        fields = '__all__'
        
class BookEventForm(ModelForm):
    class Meta:
        model=Bookevent
        fields ='__all__'
    
       