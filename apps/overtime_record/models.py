from django.db import models


class OvertimeRecord(models.Model):
    class Meta:
        verbose_name = "Registro Hora Extra"
        verbose_name_plural = "Registros Hora Extra"

    motive = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.motive
