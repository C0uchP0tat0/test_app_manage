from django.contrib import admin

from .models import Employee, Skill, EmployeeSkill

admin.site.register(Employee)
admin.site.register(Skill)
admin.site.register(EmployeeSkill)