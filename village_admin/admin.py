from django.contrib import admin
from .models import Announcements, Petcategory, VehicleCategory

# Register your models here.
admin.site.register(Announcements)
admin.site.register(Petcategory)
admin.site.register(VehicleCategory)