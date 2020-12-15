from django.db import models


# Create your models here.

class employees(models.Model):
    firstname = models.CharField(max_length=60)
    secondname = models.CharField(max_length=60)
    empid = models.IntegerField()

    def __str__(self):
        return self.firstname
