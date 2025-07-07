from django.forms import fields  
from .models import StudentModel 
from django import forms  
class StudentForm(forms.ModelForm):  
    class Meta:  
        model = StudentModel  # To specify the model to be used to create form
        fields = '__all__'  # It includes all the fields of model
