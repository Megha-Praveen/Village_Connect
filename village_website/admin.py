from django.contrib import admin
from .models import UserInfo, Members, Pets, Vehicle, Complaints, Visitors, Posts

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Members)
admin.site.register(Pets)
admin.site.register(Vehicle)
admin.site.register(Complaints)
admin.site.register(Visitors)
admin.site.register(Posts)