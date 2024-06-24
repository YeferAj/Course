from django import forms
from . models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = {'status'}
        labels ={
            'first_name': 'Nombre completo',
            'last_name': 'Apellidos',
            'document': 'Documento',
            'email': 'Correo electrónico',
            'status': 'Correo electrónico'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Ingrese los apellidos'}),
            'document': forms.TextInput(attrs={'placeholder': 'Ingrese el número de documento'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Ingrese su email', 'type': 'email'}),
        }