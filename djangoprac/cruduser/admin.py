from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll_no', 'city']

# Register the Student model with the StudentAdmin class
admin.site.register(Student, StudentAdmin)
