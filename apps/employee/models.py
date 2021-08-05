from django.contrib.auth.models import User
from django.db import models

from apps.company.models import Company
from apps.department.models import Department


class Employee(models.Model):
    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"
    name = models.CharField(max_length=100, verbose_name="Nome")
    user = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name="Usuário")
    department = models.ManyToManyField(Department, verbose_name="Departamento")
    company = models.ForeignKey(Company, on_delete=models.PROTECT, verbose_name="Empresa")

    def __str__(self) -> str:
        return self.name
