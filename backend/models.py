from django.db import models

# Create your models here.
class customer(models.Model):
    objects = None
    Name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Contactnumber = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)

class carcategory(models.Model):
    objects = None
    Name = models.CharField(max_length=100, null=True, blank=True)
    Desc = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)

class serdetails(models.Model):
    objects = None
    category = models.CharField(max_length=100, null=True, blank=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    selcar = models.CharField(max_length=100, null=True, blank=True)
    manfact = models.CharField(max_length=100, null=True, blank=True)
    fuel = models.CharField(max_length=100, null=True, blank=True)
    Desc = models.CharField(max_length=100, null=True, blank=True)
    price = models.CharField(max_length=100, null=True, blank=True)
    QUANTITY = models.IntegerField(null=True, blank=True)
    phone  = models.IntegerField()
    Image = models.ImageField(upload_to="profile", null=True, blank=True)

class msgdb(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    mail = models.EmailField(max_length=100, null=True, blank=True)
    sub =  models.CharField(max_length=100, null=True, blank=True)
    messge = models.CharField(max_length=100, null=True, blank=True)

class cartdb(models.Model):
    PDCTNAME = models.CharField(max_length=50, null=True, blank=True)
    CATEGORY = models.CharField(max_length=100, null=True, blank=True)
    PRIZE = models.IntegerField(null=True, blank=True)
    IMAGE = models.ImageField(upload_to="cart", null=True, blank=True)
    QUANTITY = models.CharField(max_length=50, null=True, blank=True)


class appointmentdb(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Phonenumber = models.IntegerField(null=True, blank=True)
    Emailadress = models.CharField(max_length=100,null=True,blank=True)
    proddb= models.IntegerField(null=True, blank=True)
    Time= models.TimeField(max_length=500, null=True, blank=True)
    Date= models.DateField(max_length=500, null=True, blank=True)
    QUANTITY = models.CharField(max_length=50, null=True, blank=True)
    LOCATION = models.CharField(max_length=100,null=True,blank=True)
    PAYMENT = models.CharField(max_length=100,null=True,blank=True)

