from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
import csv

from app.models import Employee, Skill, EmployeeSkill

class Command(BaseCommand):
    def handle(self, *args, **options):
        if options['employee']:
            with open("employees_db.csv", encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file, delimiter=",")
                for row in file_reader:
                    try:
                        created = Employee.objects.get_or_create(
                            code=row[0],
                            first_name=row[1],
                            surname=row[2],
                            is_active=row[3])
                        if created[1] == True:
                            self.stdout.write(f'Сотрудник "{created[0]}" добавлен.')
                        else:
                            self.stdout.write('Измения в базу данных не были внесены')
                    except IntegrityError:     
                        self.stderr.write('Изменения не могут быть выполнены!')

        if options['skill']:
            with open("skills_db.csv", encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file, delimiter = ",")
                for row in file_reader:
                    try:
                        created = Skill.objects.get_or_create(
                            code=row[0],
                            name=row[1],
                            description=row[2])
                        if created[1] == True:
                            self.stdout.write(f'Навык "{created[0]}" добавлен.')
                        else:
                            self.stdout.write('Измения в базу данных не были внесены')
                    except IntegrityError:      
                        self.stderr.write('Изменения не могут быть выполнены!')

        if options['empl_skill']:
            with open("employee_skills_db.csv", encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file, delimiter=",")
                for row in file_reader:
                    try:
                        created = EmployeeSkill.objects.get_or_create(
                            employee=Employee.objects.get(first_name=row[0]),
                            skill=Skill.objects.get(name=row[1]),
                            level=row[2])
                        if created[1] == True:
                            self.stdout.write(f'Изменения в базе данных "{created}" .')
                        else:
                            self.stdout.write('Измения в базу данных не были внесены')
                    except ObjectDoesNotExist:     
                        self.stderr.write('Изменения не могут быть выполнены!')

        else:
            self.stdout.write('введите команду -h или --help')

    def add_arguments(self, parser):
        parser.add_argument(
        '-e', 
        '--employee',
        action='store_true', 
        default=False,
        help='Внесение изменений в базу данных Employee'
        )
        parser.add_argument(
        '-s', 
        '--skill',
        action='store_true', 
        default=False,
        help='Внесение изменений в базу данных Skill'
        )
        parser.add_argument(
        '-es', 
        '--empl_skill',
        action='store_true', 
        default=False,
        help='Внесение изменений в базу данных EmployeeSkill'
        )