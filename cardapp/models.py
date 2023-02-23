from django.db import models
from django import forms
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth.models import User


class userInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    national_number=models.IntegerField(blank=False,null=False)
    phone=models.IntegerField(blank=False,null=False)
    email=models.EmailField(blank=True,null=True,)
    username=models.CharField(max_length=25,blank=False,null=False)
    password=models.CharField(max_length=25,blank=False,null=False)
    def __str__(self,):
        return str(self.user.username)
    
class card(models.Model):
    centers=[('Bahri','Bahri'),('Khartoum','Khartoum'),('Omdurman','Omdurman')]
    card_center=models.CharField(max_length=25,choices=centers,blank=True,null=True)
    status=[('waiting','waiting'),('accept','accept'),('reject','reject')]
    statu=models.CharField(max_length=25,blank=False,null=False,default='waiting',choices=status)
    card_user=models.OneToOneField(User, on_delete=models.CASCADE)
    FirstName=models.CharField(max_length=25,blank=False,null=False)
    SecondName=models.CharField(max_length=25,blank=False,null=False)
    ThirdName=models.CharField(max_length=25,blank=False,null=False)
    FourtName=models.CharField(max_length=25,blank=False,null=False)
    Birthdate=models.DateField()
    Placeof_Birth=models.CharField(max_length=25,blank=False,null=False)
    Blood_Type=models.CharField(max_length=25,blank=False,null=False)
    Job=models.CharField(max_length=25,blank=False,null=False)
    Address=models.CharField(max_length=25,blank=False,null=False)
    Phone=models.CharField(max_length=25,blank=False,null=False)
    Old_id=models.CharField(max_length=25,blank=False,null=False,unique=True)
    card_date=models.DateField(blank=True,auto_now_add=True)
    date_of_expiry=models.DateField(blank=True,null=True)
    date_of_accept=models.DateField(blank=True,null=True)
    date_of_reject=models.DateField(blank=True,null=True)


class Payment(models.Model):
    payment_Notification=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    process_number=models.IntegerField(blank=True, null=True)
    payment_date=models.DateField(auto_now=True)
    card=models.ForeignKey("card", on_delete=models.CASCADE)

    
#forignkey
class requestes_id(models.Model):
    req=models.ForeignKey("card", on_delete=models.CASCADE)
    def __str__(self):
        return self.FirstName


class Report(models.Model):
    start_date=models.DateField()
    end_date=models.DateField()
    card=models.ForeignKey("card", on_delete=models.CASCADE)

        