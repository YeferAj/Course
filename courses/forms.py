from django import forms
from .models import Course
from datetime import date
from .models import Enrollment
from students.models import Student




class CourseForm(forms.ModelForm):
    class Meta:
        model = Course   
        fields = ['name', 'description', 'start_date', 'end_date']
        labels = {
            "name": "Nombre del curso",
            "description": "Descripción del curso",
            "start_date": "Fecha de inicio",
            "end_date": "Fecha de finalización",
        }
        widgets ={
            "name": forms.TextInput(attrs={'placeholder': 'Ingrese el nombre del curso'}),
            'start_date': forms.DateInput(attrs={'type': 'date',
                'min': date.today().isoformat() 
            }),
            'end_date': forms.DateInput(attrs={'type': 'date',
                'min': date.today().isoformat()  
            }),
        }
    
class EnrollmentForm(forms.ModelForm):
    student = forms.ModelChoiceField(queryset=Student.objects.filter(status=True), label="Select Student")

    class Meta:
        model = Enrollment
        fields = ['student']
        