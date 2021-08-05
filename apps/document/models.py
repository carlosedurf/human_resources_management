from django.db import models

from apps.employee.models import Employee


class Document(models.Model):
    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"

    description = models.CharField(max_length=100, verbose_name="Descrição")
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, verbose_name="Pertence ao Funcionário")

    def __str__(self) -> str:
        return self.description
