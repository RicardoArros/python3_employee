# Generated by Django 3.2.8 on 2022-07-24 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0014_alter_employee_employee_companydate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_companyDate',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de ingreso (dd/mm/yyyy)'),
        ),
    ]