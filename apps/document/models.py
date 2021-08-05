from django.db import models


class Document(models.Model):
    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"

    description = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.description
