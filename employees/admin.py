from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'department', 'salary')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('department',)
