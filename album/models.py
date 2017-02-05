from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


# Create your models here.
from django.core.urlresolvers import reverse


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('lista-categorias')


class Foto(models.Model):
    categoria = models.ForeignKey(Categoria, null=True, blank=True)
    titulo = models.CharField(max_length=50, default='Sin titulo')
    foto = models.ImageField(upload_to='fotografias/')
    fecha_pub = models.DateField(auto_now_add=True)
    favorita = models.BooleanField(default=False)
    comentario = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('lista-fotos')


@receiver(post_delete, sender=Foto)
def foto_delete(sender, instance, **kwargs):
    # Borra los ficheros de las fotos que se eliminan.
    instance.foto.delete(False)
