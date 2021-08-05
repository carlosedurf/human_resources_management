from django.db import models


class Department(models.Model):
    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"

    name = models.CharField(max_length=70, verbose_name="Nome")

    def __str__(self) -> str:
        return self.name
