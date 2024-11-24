from django.urls import path
from.import views 

urlpatterns = [
    path('',views.index,name="index"),
    path('register',views.register,name="register"),
    path('login',views.loginview,name="login"),
    path('visitors',views.visitors,name="visitors"),
    path('home',views.home,name="home"),
    path('member/',views.member,name="member"),
    path('pet/',views.pet,name="pet"),
    path('vehicle/',views.vehicle,name="vehicle"),
    path('complaint',views.complaint,name="complaint"),
    path('posts',views.posts,name="posts"),
    path('edit_member/<int:member_id>/', views.edit_member, name='edit_member'),
    path('edit_pet/<int:pet_id>/', views.edit_pet, name='edit_pet'),
    path('edit_vehicle/<int:vehicle_id>/', views.edit_vehicle, name='edit_vehicle'),
]