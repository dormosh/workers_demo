from django.db import models

# Create your models here.

class Workers(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    hire_date = models.DateField()
    #job = models.IntegerField()
    salary = models.FloatField()
    commission_pct = models.FloatField()
    manager_id = models.IntegerField()
    department_id = models.IntegerField(null=True)

    def __str__(self):
        return self.employee_id


class Job(models.Model):
    name = models.CharField(max_length=50)
    jobs = models.ManyToManyField('Workers', related_name='jobs', blank=True)

    def __str__(self):
        return self.name

