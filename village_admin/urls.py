from django.urls import path
from.import views 

urlpatterns = [
    path('adminhome',views.adminhome,name="adminhome"),
    path('adminlog',views.adminlog,name="adminlog"),
    path('adminusers',views.adminusers,name="adminusers"),
    path('admincomp',views.admincomp,name="admincomp"),
    path('adminannou',views.adminannou,name="adminannou"),
    path('adminpet',views.adminpet,name="adminpet"),
    path('adminvehicle',views.adminvehicle,name="adminvehicle"),
    path('petcategories/<int:pk>/edit/', views.edit_petcategory, name='edit_petcategory'),
    path('vehiclecategories/<int:pk>/edit/', views.edit_vehiclecategory, name='edit_vehiclecategory'),
]