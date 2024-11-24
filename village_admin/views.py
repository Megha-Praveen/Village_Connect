from django.shortcuts import get_object_or_404, render, redirect
from .forms import PetCategoryForm, VehicleCategoryForm
from .models import Announcements, Petcategory, VehicleCategory
from village_website.models import Complaints, Visitors
from village_website.models import UserInfo

# Create your views here.
def adminhome(request):
    petcategories = Petcategory.objects.all()
    vehicle_categories = VehicleCategory.objects.all()
    visitors = Visitors.objects.all()
    return render(request, 'adminhome.html', {'visitors':visitors,'petcategories': petcategories, 'vehicle_categories': vehicle_categories})

def edit_petcategory(request, pk):
    petcategory = Petcategory.objects.get(pk=pk)
    if request.method == 'POST':
        # Handle form submission
        # Assuming you have a PetCategoryForm defined in forms.py
        form = PetCategoryForm(request.POST, instance=petcategory)
        if form.is_valid():
            form.save()
            return redirect('adminhome')  # Redirect to appropriate page
    else:
        # Display edit form
        form = PetCategoryForm(instance=petcategory)
    return render(request, 'edit_petcategory.html', {'form': form})

def edit_vehiclecategory(request, pk):
    vehiclecategory = VehicleCategory.objects.get(pk=pk)
    if request.method == 'POST':
        # Handle form submission
        # Assuming you have a VehicleCategoryForm defined in forms.py
        form = VehicleCategoryForm(request.POST, instance=vehiclecategory)
        if form.is_valid():
            form.save()
            return redirect('adminhome')  # Redirect to the list view
    else:
        # Display edit form
        form = VehicleCategoryForm(instance=vehiclecategory)
    return render(request, 'edit_vehiclecategory.html', {'form': form})

def adminlog(request):
    return render(request, 'adminlog.html')

def adminusers(request):
    users = UserInfo.objects.all()
    return render(request, 'adminusers.html', {'users': users})

def admincomp(request):
    complaints = Complaints.objects.all()
    return render(request, 'admincomp.html', {'complaints':complaints})

def adminannou(request):
    if request.method == 'POST':
        title = request.POST.get('title') 
        announcements = request.POST.get('announcements')

        # Save the title details to the database
        announcements = Announcements.objects.create(
            title=title,
            announcements=announcements
        )

        # Redirect to a success page or another appropriate URL
        return redirect('adminannou')# Replace 'success_page' with the desired URL name or path
    
    return render(request, 'adminannou.html')

def adminpet(request):
    if request.method == 'POST':
        pettype = request.POST.get('pettype') 

        # Save the pettype details to the database
        petcategories = Petcategory.objects.create(
            pettype=pettype,
        )

        # Redirect to a success page or another appropriate URL
        return redirect('adminhome')# Replace 'success_page' with the desired URL name or path
    
    return render(request, 'adminpet.html')



def adminvehicle(request):
    if request.method == 'POST':
        vehicle_type = request.POST.get('vehicle_type')
        # Save the vehicle type to the database
        VehicleCategory.objects.create(vehicle_type=vehicle_type)
        # Redirect back to the admin home page after adding the new category
        return redirect('adminhome')  # Redirect to the admin home page
    return render(request, 'adminvehicle.html')
