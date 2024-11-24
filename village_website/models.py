# village_website/models.py

from django.db import models
from django.contrib.auth.models import User
from village_admin.models import Petcategory, VehicleCategory

class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=100)
    housenumber = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100)
    mobilenumber = models.IntegerField()
    wardnumber = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=8)

    def __str__(self):
        return self.username
    
class Members(models.Model):
    userinfo = models.ForeignKey(UserInfo, on_delete=models.CASCADE, null=True)
    fullname = models.CharField(max_length=100)
    age = models.IntegerField()
    occupation = models.CharField(max_length=100)
    mobilenumber = models.IntegerField()
    relationship = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    bloodgroup = models.CharField(max_length=10)

class Visitors(models.Model):
    userinfo = models.ForeignKey(UserInfo,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    mobilenumber = models.IntegerField()

class Pets(models.Model):
    userinfo = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    petname = models.CharField(max_length=100)
    pettype = models.ForeignKey(Petcategory, on_delete=models.CASCADE, null=True)

class Vehicle(models.Model):
    userinfo = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    vehicle_number = models.CharField(max_length=100)
    vehicle_type = models.ForeignKey(VehicleCategory, on_delete=models.CASCADE, null=True)
    vehicle_img = models.ImageField(upload_to='vehicles/')
    
class Complaints(models.Model):
    name = models.CharField(max_length=100)
    complaints = models.CharField(max_length=500)    

class Posts(models.Model):
    userinfo = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='posts/')
