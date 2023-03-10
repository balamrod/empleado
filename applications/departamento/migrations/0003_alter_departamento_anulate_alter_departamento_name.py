# Generated by Django 4.1.5 on 2023-02-21 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0002_rename_departameento_departamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='anulate',
            field=models.BooleanField(default=False, unique=True, verbose_name='Anular'),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre'),
        ),
    ]
