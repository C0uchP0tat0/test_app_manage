from django.shortcuts import render
import csv
from django.http import HttpResponse

from .models import Employee, Skill, EmployeeSkill

def create_csv(request):
    employees = Employee.objects.all()
    empl_code=[]
    empl_first_name=[]
    empl_surname=[]
    empl_is_active=[]
    for employee in employees:
        empl_code.append(employee.code)
        empl_first_name.append(employee.first_name)
        empl_surname.append(employee.surname)
        empl_is_active.append(employee.is_active)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="employees_db.csv"'

    writer = csv.writer(response)
    writer.writerow(empl_code)
    writer.writerow(empl_first_name)
    writer.writerow(empl_surname)
    writer.writerow(empl_is_active)

    return response