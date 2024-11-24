# forms.py

from django import forms
from .models import Vehicle, Members, Pets

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vehicle_number', 'vehicle_type', 'vehicle_img']

class MemberForm(forms.ModelForm):
    class Meta:
        model = Members
        fields = ['fullname', 'age', 'occupation', 'mobilenumber', 'relationship', 'qualification', 'bloodgroup']

class PetForm(forms.ModelForm):
    class Meta:
        model = Pets
        fields = ['petname', 'pettype']
