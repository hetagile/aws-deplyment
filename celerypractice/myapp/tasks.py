from celery import shared_task
from .models import Student

@shared_task
def add_stud(count):
    objects_to_append = []
    for i in range(1,count+1):
        objects_to_append.append(Student(name='thor', roll_no=i))
        
    Student.objects.bulk_create(objects_to_append)

@shared_task
def delete_stud():
    print('............................................delette')
    Student.objects.all().delete()

@shared_task(bind=True)
def add(self, x, y):
    print('x + y: ', x + y)
    z = int(x) + int(y)
    return z