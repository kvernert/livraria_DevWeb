from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
    def __str__(self):
        return self.nome