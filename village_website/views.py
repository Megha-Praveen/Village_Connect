from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from village_admin.models import Announcements
from village_website.forms import VehicleForm, MemberForm, PetForm
from .models import UserInfo, Members, Pets, Vehicle, Complaints, Visitors, Posts
from village_admin.models import Petcategory, VehicleCategory
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    announcements = Announcements.objects.all()
    posts = Posts.objects.all()
    return render(request, 'index.html', {'announcements': announcements, 'posts':posts})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        mobile_no = request.POST['mobilenumber']
        house_no = request.POST['housenumber']
        ward_no = request.POST['wardnumber']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('register')
        else:
            user = User.objects.create_user(username=email,email=email,first_name=username,password=password)
            user.first_name=username
            user.save()
            info = UserInfo()
            info.wardnumber=ward_no
            info.mobilenumber=mobile_no
            info.housenumber=house_no
            info.user=user
            info.username=username
            info.email=email
            # .objects.create(ward_no=ward_no, phone_no=mobile_no, house_no=house_no, user=user)
            info.save()

            # Log the user in after registration
            # login(request, user)

            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('login')
    else:
        return render(request, 'register.html')


def loginview(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email,password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('adminhome')
            else:
                return redirect('home')

        else:
            messages.success(request,'Invalid Username or Password')

            return render(request, 'login.html')
    return render(request,'login.html')


def visitors(request):
    if request.method == 'POST':
        name = request.POST.get('name') 
        email = request.POST.get('email')
        address = request.POST.get('address')
        mobilenumber = request.POST.get('mobilenumber')
        

        # Save the title details to the database
        visitors = Visitors.objects.create(
            name=name,
            email=email,
            address=address,
            mobilenumber=mobilenumber, 
        )

        # Redirect to a success page or another appropriate URL
        return redirect('/')# Replace 'success_page' with the desired URL name or path

    return render(request, 'visitors.html')

def home(request):
    abc = UserInfo.objects.get(user_id=request.user.id)

    members = Members.objects.filter(userinfo_id=abc.id)
    pets = Pets.objects.filter(userinfo_id=abc.id)
    vehicles = Vehicle.objects.filter(userinfo_id=abc.id)

    return render(request, 'home.html',{'members':members,'pets':pets,'vehicles':vehicles})

def member(request):
    abc = UserInfo.objects.get(user_id=request.user.id)

    if request.method == 'POST':
        fullname = request.POST.get('fullname') 
        age = request.POST.get('age')
        occupation = request.POST.get('occupation')
        relationship = request.POST.get('relationship')
        mobilenumber = request.POST.get('mobilenumber')
        qualification = request.POST.get('qualification')
        bloodgroup = request.POST.get('bloodgroup')

        # Save the title details to the database
        members = Members.objects.create(
            userinfo_id=abc.id,
            fullname=fullname,
            age=age,
            occupation=occupation,
            mobilenumber=mobilenumber,
            relationship=relationship,
            qualification=qualification,
            bloodgroup=bloodgroup,
        )

        # Redirect to a success page or another appropriate URL
        return redirect('home')# Replace 'success_page' with the desired URL name or path
    
    return render(request, 'member.html')

def pet(request):
    abc = UserInfo.objects.get(user_id=request.user.id)

    if request.method == 'POST':
        petname = request.POST.get('petname') 
        pettype = request.POST.get('pettype')

        try:
            petcategory = Petcategory.objects.get(id=pettype)
        except Petcategory.DoesNotExist:
            pass
        else:
            pet = Pets.objects.create(
                userinfo=abc,  # Associate the pet with the current user's UserInfo
                petname=petname,
                pettype=petcategory,
            )
        return redirect('pet')  # Redirect to the home page after successfully adding the pet
    else:
        petcategories = Petcategory.objects.all()
        return render(request, 'pet.html',{'petcategories':petcategories})

def vehicle(request):
    # Retrieve the UserInfo instance for the current user
    abc = UserInfo.objects.get(user_id=request.user.id)

    if request.method == 'POST':
        # Handle form submission and save the new vehicle
        vehicle_number = request.POST.get('vehicle_number')
        vehicle_type_id = request.POST.get('vehicle_type')
        vehicle_img = request.FILES.get('vehicle_img')
        vehicle_type = VehicleCategory.objects.get(id=vehicle_type_id) if vehicle_type_id else None

        # Create the vehicle object
        vehicle = Vehicle.objects.create(
            userinfo=abc,  # Associate the vehicle with the current user's UserInfo
            vehicle_number=vehicle_number,
            vehicle_type=vehicle_type,
            vehicle_img=vehicle_img
        )
        # Redirect to the same page after adding the vehicle
        return redirect('vehicle')
    else:
        # Fetch all vehicle categories for the form
        vehicle_categories = VehicleCategory.objects.all()
        return render(request, 'vehicle.html', {'vehicle_categories': vehicle_categories})
    
def edit_member(request, member_id):
    member = get_object_or_404(Members, id=member_id)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the members page after editing
    else:
        form = MemberForm(instance=member)
    return render(request, 'edit_member.html', {'form': form})

def edit_pet(request, pet_id):
    pet = get_object_or_404(Pets, id=pet_id)
    if request.method == 'POST':
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the pets page after editing
    else:
        form = PetForm(instance=pet)
    return render(request, 'edit_pet.html', {'form': form})
    
def edit_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'edit_vehicle.html', {'form': form})
    
def complaint(request):
    if request.method == 'POST':
        name = request.POST.get('name') 
        complaints = request.POST.get('complaints')

        # Save the title details to the database
        complaints = Complaints.objects.create(
            name=name,
            complaints=complaints
        )

        # Redirect to a success page or another appropriate URL
        return redirect('complaint')# Replace 'success_page' with the desired URL name or path
    
    return render(request, 'complaint.html')

def posts(request):
    abc = UserInfo.objects.get(user_id=request.user.id)

    if request.method == 'POST':
        title = request.POST.get('title') 
        desc = request.POST.get('desc')
        img = request.FILES.get('img')

        # Save the title details to the database
        posts = Posts.objects.create(
            userinfo_id=abc.id,
            title=title,
            desc=desc,
            img=img,
        )

        # Redirect to a success page or another appropriate URL
        return redirect('/')# Replace 'success_page' with the desired URL name or path
    
    return render(request, 'posts.html')

