from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from . forms import CourseForm, EnrollmentForm
from django.contrib import messages
from .models import Course, Enrollment

# Create your views here.
def courses(request):
    form = CourseForm(request.POST or None)
    courses = Course.objects.all()
    if form.is_valid() and request.method == 'POST':
        try:
            form.save()
            messages.success(request, 'Curso registrado con éxito.')
            return redirect('courses')
        except:
            messages.error(request, 'Ocurrió un error al registrar el curso.')
            return redirect('courses')
    return render(request, "courses/index.html", {'form': form, 'courses': courses })


def delete_course(request, id):
    course = Course.objects.get(id=id)
    try:
        course.delete()
        messages.success(request, 'Curso eliminado con éxito')
        return redirect('courses')
    except:
        messages.error(request, 'Error al eliminar el curso')
        return redirect('courses')   

def edit_course(request, id):
    course = Course.objects.get(id=id)
    form = CourseForm(request.POST or None, instance=course)
    if form.is_valid() and request.method == 'POST':
        try:
            form.save()
            messages.success(request, 'Curso actualizado con éxito.')
            return redirect('courses')
        except:
            messages.error(request, 'Ocurrió un error al actualizar el curso.')
            return redirect('courses')
    return render(request, "courses/edit.html", {'form': form, 'course': course})


def index1(request):
    # lógica para obtener los estudiantes
    return render(request, 'courses/index.html')


def course_detail(request, id):
    course = get_object_or_404(Course, id=id)
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.course = course
            enrollment.save()
            return redirect('course_detail', id=course.id)
    else:
        form = EnrollmentForm()
    
    enrolled_students = Enrollment.objects.filter(course=course)
    return render(request, 'courses/view.html', {'course': course, 'form': form, 'enrolled_students': enrolled_students})




def add_enrollment(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Estudiante matriculado exitosamente en el curso..')
            return redirect('enrollment_list')
        else:
            messages.error(request, 'Se produjo un error al inscribir al estudiante..')
    else:
        form = EnrollmentForm()
    return render(request, 'courses/add_enrollment.html', {'form': form})



def enrollment_list(request):
    enrollments = Enrollment.objects.all()
    return render(request, 'courses/enrollment_list.html', {'enrollments': enrollments})

