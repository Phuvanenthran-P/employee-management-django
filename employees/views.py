from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm
from django.shortcuts import get_object_or_404

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/list.html', {'employees': employees})

def employee_create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()

    return render(request, 'employees/create.html', {'form': form})

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'employees/update.html', {
        'form': form,
        'employee': employee
    })

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == "POST":
        employee.delete()
        return redirect('employee_list')

    return render(request, 'employees/delete.html', {'employee': employee})
