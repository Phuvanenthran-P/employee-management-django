from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'department', 'salary']

    def clean_salary(self):
        salary = self.cleaned_data.get('salary')
        if salary < 0:
            raise forms.ValidationError("Salary cannot be negative.")
        return salary


