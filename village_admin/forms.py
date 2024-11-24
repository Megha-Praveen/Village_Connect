from django import forms
from .models import Petcategory, VehicleCategory

class PetCategoryForm(forms.ModelForm):
    class Meta:
        model = Petcategory
        fields = ['pettype']  # Specify the fields you want to include in the form
        labels = {'pettype': 'Pet Type'}  # Optionally, provide custom labels for the fields

class VehicleCategoryForm(forms.ModelForm):
    class Meta:
        model = VehicleCategory
        fields = ['vehicle_type']  # Specify the fields you want to include in the form