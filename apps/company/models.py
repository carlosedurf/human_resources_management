from django.db import models


class Company(models.Model):
    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
    name = models.CharField(max_length=100, help_text="Nome da Empresa")

    def __str__(self) -> str:
        return self.name
