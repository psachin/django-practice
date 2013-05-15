from django.db import models
from django.forms import ModelForm
# Create your models here.
class Calc(models.Model):
    field1 = models.IntegerField(max_length=10)
    field2 = models.IntegerField(max_length=10)

class CalcForm(ModelForm):
    class Meta:
        model = Calc




