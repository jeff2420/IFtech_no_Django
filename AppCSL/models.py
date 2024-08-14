from django.db import models

class Movimento(models.Model):
    veículo = models.CharField(max_length=20)  
    data = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"{self.veículo} - {self.data} - {self.hora}"