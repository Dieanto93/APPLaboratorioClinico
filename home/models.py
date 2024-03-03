from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator
from django.db import models

class Administrativo(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    # Agrega más campos según sea necesario

    def __str__(self):
        return str(self.usuario)

class Tecnico(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    # Agrega más campos según sea necesario

    def __str__(self):
        return str(self.usuario)
    
class Paciente(models.Model):
    cedula = models.CharField(max_length=10, validators=[MaxLengthValidator(10)], null=True, blank=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.cedula
    
class Examen_disponible(models.Model):
    nombre_examen = models.CharField(max_length=100)
    unidad = models.CharField(max_length=10, null=True, blank=True)
    area = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nombre_examen
    
class Pedido_examen(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='pedidos_examenes')
    fecha = models.DateField(auto_now_add=True)
    pendiente = models.BooleanField(default=True)  # Nuevo campo para indicar si el pedido está pendiente o procesado
    examenes_disponibles = models.ManyToManyField(Examen_disponible, related_name='pedidos_examenes')  # Relación muchos a muchos con Examen_disponible

    def __str__(self):
        return f"Pedido para {self.paciente} - {self.fecha}"
    
class Resultado_examen(models.Model):
    pedido_examen = models.ForeignKey(Pedido_examen, on_delete=models.CASCADE, related_name='resultados_examenes')
    nombre_examen = models.ForeignKey(Examen_disponible, on_delete=models.CASCADE)
    valor_resultado = models.FloatField(null=True, blank=True)
    rango = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return f"Resultado para {self.pedido_examen} - {self.pedido_examen}"
    


    