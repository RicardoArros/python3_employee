from django.db import models

# Create your models here.

class Employee(models.Model):
  #id = models.AutoField(primary_key=True)
  employee_rut = models.CharField(max_length=50, primary_key=True)
  employee_firstname = models.CharField(max_length=50, verbose_name="Nombres", null=True)
  employee_lastname = models.CharField(max_length=50, verbose_name="Apellidos", null=True)
  employee_address = models.CharField(max_length=60, verbose_name="Dirección", null=True)
  employee_phone = models.CharField(max_length=30, verbose_name="Teléfono", null=True)
  employee_gender	= models.CharField(max_length=30, verbose_name="Género", null=True)
  employee_companyDate = models.DateField()

  perfil_id = models.ForeignKey("Profile", verbose_name=(""), on_delete=models.CASCADE)
  area_id = models.ForeignKey("Area", verbose_name=(""), on_delete=models.CASCADE)
  dep_id = models.ForeignKey("Department", verbose_name=(""), on_delete=models.CASCADE)
  position_id = models.ForeignKey("Position", verbose_name=(""), on_delete=models.CASCADE)

  def __str__(self):
    return self.employee_firstname


class Profile(models.Model):
  perfil_id = models.AutoField(primary_key=True)
  perfil_name = models.CharField(max_length=30, verbose_name="Nombre Perfil", null=True)


class Area(models.Model):
  area_id = models.AutoField(primary_key=True)
  area_name = models.CharField(max_length=30, verbose_name="Nombre Area", null=True)


class Department(models.Model):
  dep_id = models.AutoField(primary_key=True)
  dep_name = models.CharField(max_length=30, verbose_name="Nombre Departamento", null=True)

  area_id = models.ForeignKey("Area", verbose_name=(""), null=True, on_delete=models.CASCADE)


class Position(models.Model):
  position_id = models.AutoField(primary_key=True)
  position_name = models.CharField(max_length=30, verbose_name="Nombre Cargo", null=True)

  dep_id = models.ForeignKey("Department", verbose_name=(""), null=True, on_delete=models.CASCADE)


class ContactEmergency(models.Model):  
  contact_id = models.AutoField(primary_key=True)
  contact_relation = models.CharField(max_length=50, verbose_name="Relación Parentesca", null=True)
  contact_phone = models.CharField(max_length=30, verbose_name="Teléfono", null=True)
  contact_firstname = models.CharField(max_length=50, verbose_name="Nombres", null=True)
  contact_lastname = models.CharField(max_length=50, verbose_name="Apellidos", null=True)

  employee_rut = models.ForeignKey("Employee", verbose_name=(""), null=True, on_delete=models.CASCADE)


class Liability(models.Model):  
  liability_id = models.AutoField(primary_key=True)
  liability_rut = models.CharField(max_length=50, verbose_name="Rut Carga", null=True)
  liability_firstname = models.CharField(max_length=60, verbose_name="Nombre Carga", null=True)
  liability_lastname = models.CharField(max_length=50, verbose_name="Apellido Carga", null=True)  
  liability_gender = models.CharField(max_length=30, verbose_name="Género Carga", null=True)
  liability_kin = models.CharField(max_length=50, verbose_name="Parentesco Carga", null=True)

  employee_rut = models.ForeignKey("Employee", verbose_name=(""), null=True, on_delete=models.CASCADE)

