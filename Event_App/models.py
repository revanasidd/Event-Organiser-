from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Family Class
class Family(models.Model):
    Event_type =models.CharField(max_length=200)
    Desc = models.TextField(max_length=1200)
    Image = models.ImageField(upload_to='static/image/family_images')
    Food = models.CharField(max_length=200)
    Decoration = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default='')

    def __str__(self) -> str:
        return self.Event_type

# Culture
class Culture(models.Model):
    Event_type =models.CharField(max_length=200)
    Desc = models.TextField(max_length=1200)
    Image = models.ImageField(upload_to='static/image/ulture_images')
    Food = models.CharField(max_length=200)
    Decoration = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default='')

    def __str__(self) -> str:
        return self.Event_type

# Bussiness
class Bussiness(models.Model):
    Event_type =models.CharField(max_length=200)
    Desc = models.TextField(max_length=1200)
    Image = models.ImageField(upload_to='static/image/bussiness_images')
    Food = models.CharField(max_length=200)
    Publicity = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default='')
    
    def __str__(self) -> str:
        return self.Event_type

# Charity
class Charity(models.Model):
    Event_type =models.CharField(max_length=200)
    Desc = models.TextField(max_length=1200)
    Image = models.ImageField(upload_to='charity_images')
    Food = models.CharField(max_length=200)
    Sponser = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default='')

    def __str__(self) -> str:
        return self.Event_type
#Book_Event
class Bookevent(models.Model):
    Name = models.CharField(max_length=200)
    Mobile = models.IntegerField(blank=False, null=True)
    Loaction = models.CharField(max_length=200)
    Email = models.EmailField(blank=True, null=True)
    Pepole = models.CharField(max_length=50)
    Date = models.DateField(blank=False)
    Event = models.CharField( max_length=150)
    Address = models.CharField(max_length=1200)
    Message = models.TextField(max_length=1200)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default='')

    def __str__(self) -> str:
        return self.Name

# Enquiry_Form
class Contactus(models.Model):
    Name = models.CharField(max_length=200)
    Mobile = models.IntegerField()
    Email = models.EmailField()
    Message = models.TextField()

    def __str__(self) -> str:
        return self.Name