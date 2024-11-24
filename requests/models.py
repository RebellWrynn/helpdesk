from django.db import models


class Employees(models.Model):
    Employees_id = models.CharField(primary_key='True',max_length=20)
    Firstname = models.CharField('Firstname',max_length=30)
    Lastname = models.CharField('Lastname',max_length=30)
    Surname = models.CharField('Surname',max_length=30)


class User_Requests(models.Model):
    Employees_id = models.ForeignKey(Employees,on_delete=models.CASCADE)
    Request_id = models.CharField(primary_key='True',max_length=20)
    Them = models.CharField(max_length=30)
    Requesttype = models.CharField(max_length=30)
    Priority = models.CharField(max_length=30)
    Description = models.CharField(max_length=30)
    Date = models.DateField()
    Responsibleemployee = models.CharField(max_length=30)
# Create your models here.
