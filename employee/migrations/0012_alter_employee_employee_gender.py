# Generated by Django 3.2.8 on 2022-07-24 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0011_alter_employee_employee_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_gender',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='', max_length=1, null=True, verbose_name='Género'),
        ),
    ]
