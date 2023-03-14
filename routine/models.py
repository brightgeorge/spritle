from django.db import models

# Create your models here.
class login(models.Model):
    student_id = models.CharField(max_length=100)
    student_name = models.CharField(max_length=250)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=20)
    student_description = models.TextField()
    user_flage = models.IntegerField()

class task(models.Model):
    student_id = models.CharField(max_length=250)
    task_code = models.CharField(max_length=250)
    task = models.CharField(max_length=250)
    task_description = models.TextField()
    task_answer = models.CharField(max_length=250)
    task_assigned_by = models.CharField(max_length=250)
    task_assigned_to = models.CharField(max_length=250)
    task_type = models.CharField(max_length=250)
    task_status = models.IntegerField()





