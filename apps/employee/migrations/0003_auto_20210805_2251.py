# Generated by Django 3.2.6 on 2021-08-05 22:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('department', '0002_alter_department_name'),
        ('company', '__first__'),
        ('employee', '0002_alter_employee_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='company.company', verbose_name='Empresa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ManyToManyField(to='department.Department', verbose_name='Departamento'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='auth.user', verbose_name='Usuário'),
            preserve_default=False,
        ),
    ]
