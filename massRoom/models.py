from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    description = models.TextField()
    email = models.EmailField(null=True)
    phone_number = models.BigIntegerField(null=True)
    image = models.ImageField(upload_to='staff_image')


    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='service_image')

    def __str__(self):
        return self.name

class Record(models.Model):
    #processed = 'Оброблено'
    #not_processed = 'Не оброблено'
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    comment = models.TextField()
    massage = models.CharField(max_length=200)

    def __str__(self):
        return self.massage + ' (' + self.name + ')'