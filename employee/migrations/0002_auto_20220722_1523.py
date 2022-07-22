# Generated by Django 3.2.8 on 2022-07-22 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('area_id', models.AutoField(primary_key=True, serialize=False)),
                ('area_name', models.CharField(max_length=30, null=True, verbose_name='Nombre Area')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_rut', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('employee_firstname', models.CharField(max_length=50, null=True, verbose_name='Nombres')),
                ('employee_lastname', models.CharField(max_length=50, null=True, verbose_name='Apellidos')),
                ('employee_address', models.CharField(max_length=60, null=True, verbose_name='Dirección')),
                ('employee_phone', models.CharField(max_length=30, null=True, verbose_name='Teléfono')),
                ('employee_gender', models.CharField(max_length=30, null=True, verbose_name='Género')),
                ('employee_companyDate', models.DateField()),
                ('area_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.area', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Liability',
            fields=[
                ('liability_id', models.AutoField(primary_key=True, serialize=False)),
                ('liability_rut', models.CharField(max_length=50, null=True, verbose_name='Rut Carga')),
                ('liability_firstname', models.CharField(max_length=60, null=True, verbose_name='Nombre Carga')),
                ('liability_lastname', models.CharField(max_length=50, null=True, verbose_name='Apellido Carga')),
                ('liability_gender', models.CharField(max_length=30, null=True, verbose_name='Género Carga')),
                ('liability_kin', models.CharField(max_length=50, null=True, verbose_name='Parentesco Carga')),
                ('employee_rut', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.employee', verbose_name='')),
            ],
        ),
        migrations.DeleteModel(
            name='Worker',
        ),
        migrations.AddField(
            model_name='position',
            name='dep_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.department', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='contactemergency',
            name='contact_firstname',
            field=models.CharField(max_length=50, null=True, verbose_name='Nombres'),
        ),
        migrations.AlterField(
            model_name='contactemergency',
            name='contact_lastname',
            field=models.CharField(max_length=50, null=True, verbose_name='Apellidos'),
        ),
        migrations.AlterField(
            model_name='contactemergency',
            name='contact_phone',
            field=models.CharField(max_length=30, null=True, verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='contactemergency',
            name='contact_relation',
            field=models.CharField(max_length=50, null=True, verbose_name='Relación Parentesca'),
        ),
        migrations.AlterField(
            model_name='department',
            name='dep_name',
            field=models.CharField(max_length=30, null=True, verbose_name='Nombre Departamento'),
        ),
        migrations.AlterField(
            model_name='position',
            name='position_name',
            field=models.CharField(max_length=30, null=True, verbose_name='Nombre Cargo'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='perfil_name',
            field=models.CharField(max_length=30, null=True, verbose_name='Nombre Perfil'),
        ),
        migrations.AddField(
            model_name='employee',
            name='dep_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.department', verbose_name=''),
        ),
        migrations.AddField(
            model_name='employee',
            name='perfil_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.profile', verbose_name=''),
        ),
        migrations.AddField(
            model_name='employee',
            name='position_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.position', verbose_name=''),
        ),
        migrations.AddField(
            model_name='contactemergency',
            name='employee_rut',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.employee', verbose_name=''),
        ),
        migrations.AddField(
            model_name='department',
            name='area_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.area', verbose_name=''),
        ),
    ]