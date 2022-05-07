from django.contrib import admin
from api.models import Super_Admin, Teacher, Student

# Register your models here.
admin.site.register(Super_Admin)
admin.site.register(Teacher)
admin.site.register(Student)