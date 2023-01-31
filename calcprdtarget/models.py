from django.db import models

# Create your models here.
class prdanalysis(models.Model):
    es_target = models.DecimalField(max_digits= 10,  decimal_places=0)
    ac_target = models.DecimalField(max_digits= 10, decimal_places=0)
    score = models.DecimalField(max_digits= 4, decimal_places=0)
    bonus = models.DecimalField(max_digits= 4, decimal_places=0)
    date = models.DateField()
    time = models.TimeField()
