# Generated by Django 3.2.6 on 2021-08-05 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=70, verbose_name='Nome'),
        ),
    ]
