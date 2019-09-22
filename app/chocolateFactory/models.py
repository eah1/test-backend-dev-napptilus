from django.db import models

# Create your models here.


class OompaLoompa(models.Model):
    """OompaLoompa model"""

    name = models.CharField(max_length=30, unique=False)
    age = models.IntegerField()
    job = models.CharField(max_length=50)
    height = models.DecimalField(max_digits=3, decimal_places=2)
    weight = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.name.lower()
