from django.db import models

# Create your models here.

class Employment(models.Model):
    name = models.CharField(max_length=100)
    start_salary = models.DecimalField(max_digits=10, decimal_places=2)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.position} at {self.company}"