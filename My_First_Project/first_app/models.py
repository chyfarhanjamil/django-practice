from django.db import models
from django.forms import ModelForm, Textarea

# Create your models here.


class Students(models.Model):
    # sId = models.IntegerField()
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email = models.EmailField()

    # class Meta:
    #     db_table = "students"
