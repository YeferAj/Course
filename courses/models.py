from django.db import models
from students.models import Student

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('course', 'student')
    
    def __str__(self):
        return f"{self.student} inscrito en {self.course}"