from django.db import models

class Postre(models.Model):
    nombre = models.CharField(max_length=100)
    sabor = models.CharField(max_length=50)
    tamanio = models.CharField(max_length=20)
    # Campo para cumplir el requisito de relación
    bebida_sugerida_id = models.IntegerField(null=True, blank=True) 

    def __str__(self):
        return f"{self.nombre} (Sabor: {self.sabor})"
