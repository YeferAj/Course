
from django.shortcuts import render, redirect
from . forms import StudentForm
from django.contrib import messages
from .models import Student

# Create your views here.
def students(request):
    form = StudentForm(request.POST or None)
    students = Student.objects.all()
    if form.is_valid() and request.method == 'POST':
        try:
            form.save()
            messages.success(request, 'Estudiante registrado con éxito.')
            return redirect('students')
        except:
            messages.error(request, 'Ocurrió un error al registrar el Estudiante.')
            return redirect('students')
    return render(request, "students/index.html", {'form': form, 'students': students })


def delete_student(request, id):
    student = Student.objects.get(id=id)
    try:
        student.delete()
        messages.success(request, 'Estudiante eliminado con éxito')
        return redirect('students')
    except:
        messages.error(request, 'Error al eliminar el Estudiante')
        return redirect('students')   

def edit_student(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid() and request.method == 'POST':
        try:
            form.save()
            messages.success(request, 'Estudiante actualizado con éxito.')
            return redirect('students')
        except:
            messages.error(request, 'Ocurrió un error al actualizar el Estudiante.')
            return redirect('students')
    return render(request, "students/edit.html", {'form': form, 'student': student})

def view_student(request, id):
    student =  Student.objects.get(id=id)
    return render(request, "students/view.html", {'student': student})

def index(request):
    # lógica para obtener los estudiantes
    return render(request, 'students/index.html')
