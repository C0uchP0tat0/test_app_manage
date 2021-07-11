'''Дано:
Есть данные в базе данных (или их отсутствие)
Есть csv файл с структурой соответствует одной из таблиц

Задача:
Написть команду (management/commands) которая на вход принимает 
название одной из моделей и путь к csv файлу
После приминения команды она должна вывести все изменения в базе данных которые она делает
А содержимое таблицы базы данных соответствовать содержимому файла'''

from django.db import models

class Employee(models.Model):
    code = models.TextField(max_length=20, unique=True)
    first_name = models.TextField(max_length=20)
    surname = models.TextField(max_length=50)
    is_active = models.BooleanField(null=True)

    def __str__(self):
        return self.first_name

class Skill(models.Model):
    code = models.TextField(unique=True)
    name = models.TextField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name

class EmployeeSkill(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    level = models.IntegerField()

    def __str__(self):
        return str(self.employee)
  
    class __meta__:
      unique_together = ['employee', 'skill']
