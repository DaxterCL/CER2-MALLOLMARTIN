from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'

    def __str__(self):
        return self.nombre


class LugarPatrimonial(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=200)
    anio_construccion = models.PositiveIntegerField('año de construcción')
    imagen = models.URLField('URL de la imagen', max_length=500, blank=True)

    # Relación 1:N: una categoría tiene muchos lugares.
    # PROTECT evita borrar una categoría que todavía tiene lugares asociados.
    # related_name permite usar categoria.lugares desde el lado de Categoria.
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='lugares',
    )

    class Meta:
        ordering = ['nombre']
        verbose_name = 'lugar patrimonial'
        verbose_name_plural = 'lugares patrimoniales'

    def __str__(self):
        return self.nombre
