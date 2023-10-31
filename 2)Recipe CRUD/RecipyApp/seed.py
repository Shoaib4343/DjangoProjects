from faker import Faker
fake = Faker()
import random
from .models import *

def student_subject_marks(n):
    try:
        student_objs = Student.objects.all()
        for student in student_objs:
            studnet_subject_objs = Subject.objects.all()
            for subject in studnet_subject_objs:
                StudentMarks.objects.create(
                    student=student,
                    subject = subject,
                    marks = random.randint(0,100)
                )
    except Exception as e:
        print(e)

def seed_db(n=10) -> None:
    try:
        for _ in range(n):
            department_obj =Department.objects.all()
            random_index = random.randint(0, len(department_obj)-1)
            department = department_obj[random_index]
            student_id = f'STU-0{random.randint(100, 999)}'
            student_name  = fake.name()
            student_email = fake.email()
            student_address = fake.address()
            student_age = random.randint(20,30)

            student_id_obj = StudentID.objects.create(student_id = student_id)

            student_obj=Student.objects.create(
                department = department,
                student_id  = student_id_obj,
                student_name  = student_name,
                student_email = student_email,
                student_address = student_address,
                student_age = student_age,
            )

    except Exception as e:
        print(e)

