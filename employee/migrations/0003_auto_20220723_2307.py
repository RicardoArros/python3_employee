# Generated by Django 3.2.8 on 2022-07-24 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20220722_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactemergency',
            name='employee_rut',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.employee', verbose_name='Rut trabajador'),
        ),
        migrations.AlterField(
            model_name='department',
            name='area_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.area', verbose_name='Area'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='area_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.area', verbose_name='Area'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='dep_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.department', verbose_name='Departamento'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_companyDate',
            field=models.DateField(verbose_name='Fecha de ingreso'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_gender',
            field=models.CharField(choices=[(1, 'Masculino'), (2, 'Femenino')], max_length=30, null=True, verbose_name='Género'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_rut',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Rut'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='perfil_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.profile', verbose_name='Perfil'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.position', verbose_name='Cargo'),
        ),
        migrations.AlterField(
            model_name='liability',
            name='employee_rut',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.employee', verbose_name='Rut trabajador'),
        ),
        migrations.AlterField(
            model_name='position',
            name='dep_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.department', verbose_name='Departamento'),
        ),
    ]
