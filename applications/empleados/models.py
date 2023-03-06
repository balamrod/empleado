from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField


class habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)
    
    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural ='Habilidades Empleados'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad 

# Create your models here.
class Empleado(models.Model):  

    JOB_CHOICES = (
        ('0','CONTADOR'),
        ('1','ADMINISTRATOR'),
        ('2','ECONOMISTA'),
        ('3','OTRO')
    )

    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField('Nombre completo', max_length=120, blank=True)
    job = models.CharField('Trabajo', max_length=1, choices =JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField( upload_to='empleado', height_field=None, width_field=None, max_length=None,blank=True, null = True)
    habilidades = models.ManyToManyField(habilidades)
    hoja_vida = RichTextField()

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural ='Empleados'
        ordering = ['-first_name','last_name','job']
        unique_together = ('first_name','last_name')

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name