from django.db import models


class Employee(models.Model):
    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"
    name = models.CharField(max_length=100, verbose_name="Nome")

    def __str__(self) -> str:
        return self.name
