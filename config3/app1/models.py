from django.db import models

# Create your models here.

class Course(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField
    cerated_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
class Student(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField
    enrolled_at=models.DateTimeField(auto_now=True)
    courese=models.ForeignKey(Course,on_delete=models.CASCADE)
    def __str__(self):
        return  self.name
class Comment (models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    commnet=models.TextField()
    commnet_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.student.name} on {self.course.title}"