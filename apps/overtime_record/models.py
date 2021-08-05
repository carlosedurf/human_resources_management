from django.db import models

from apps.employee.models import Employee


class OvertimeRecord(models.Model):
    class Meta:
        verbose_name = "Registro Hora Extra"
        verbose_name_plural = "Registros Hora Extra"

    motive = models.CharField(max_length=100, verbose_name="Motivo")
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, verbose_name="Funcionário")

    def __str__(self) -> str:
        return self.motive
