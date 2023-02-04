from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Event(models.Model):
    e_id = models.AutoField(primary_key=True)
    e_name = models.CharField(max_length=100)
    e_list = ArrayField(models.IntegerField(), blank=True)

    def __str__(self):
        return self.e_name