# Generated by Django 3.2.8 on 2022-07-26 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0017_alter_liability_liability_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactemergency',
            name='contact_firstname',
            field=models.CharField(max_length=50, null=True, verbose_name='Nombres Contacto de emergencia'),
        ),
        migrations.AlterField(
            model_name='contactemergency',
            name='contact_lastname',
            field=models.CharField(max_length=50, null=True, verbose_name='Apellidos Contacto de emergencia'),
        ),
        migrations.AlterField(
            model_name='contactemergency',
            name='contact_phone',
            field=models.CharField(max_length=30, null=True, verbose_name='Teléfono Contacto de emergencia'),
        ),
        migrations.AlterField(
            model_name='contactemergency',
            name='contact_relation',
            field=models.CharField(max_length=50, null=True, verbose_name='Relación Parentesca Contacto de emergencia'),
        ),
        migrations.AlterField(
            model_name='contactemergency',
            name='employee_rut',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.employee', verbose_name=''),
        ),
    ]