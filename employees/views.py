from django.shortcuts import render, redirect
from .models import Employee

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/list.html', {'employees': employees})


def employee_create(request):
    if request.method == "POST":
        Employee.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            department=request.POST['department'],
            salary=request.POST['salary'],
        )
        return redirect('employee_list')

    return render(request, 'employees/create.html')
