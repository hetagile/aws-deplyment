from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=10)
    roll_no = models.IntegerField()

    def __str__(self):
        return self.name