from django.contrib import admin

from  .models import Student,Course,Comment
# Register your models here.

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Comment)
