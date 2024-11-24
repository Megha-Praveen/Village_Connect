from django.db import models

# Create your models here.
class Announcements(models.Model):
    title = models.CharField(max_length=100)
    announcements = models.CharField(max_length=1000)

    def __str__(self):
        return self.title
    
class Petcategory(models.Model):
    pettype = models.CharField(max_length=100)
    
    def __str__(self):
        return self.pettype
    
class VehicleCategory(models.Model):
    vehicle_type = models.CharField(max_length=100)

    def __str__(self):
        return self.vehicle_type
    
    
