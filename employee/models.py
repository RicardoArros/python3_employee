from django.db import models

# Create your models here.

class Employee(models.Model):
  #
  select_gender = (
    ('M', "Masculino"),
    ('F', "Femenino")
  )
  
  employee_rut = models.CharField(max_length=50, verbose_name="Rut", primary_key=True)
  employee_firstname = models.CharField(max_length=50, verbose_name="Nombres", null=True)
  employee_lastname = models.CharField(max_length=50, verbose_name="Apellidos", null=True)
  employee_address = models.CharField(max_length=60, verbose_name="Dirección", null=True)
  employee_phone = models.CharField(max_length=30, verbose_name="Teléfono", null=True)
  employee_gender	= models.CharField(max_length=1, verbose_name="Género", null=True, choices=select_gender, default='')
  employee_companyDate = models.DateField(auto_now_add=False, auto_now=False , blank=True, verbose_name="Fecha de ingreso (dd/mm/yyyy)", null=True)
  timestamp = models.DateField(auto_now_add=True, auto_now=False , blank=True, verbose_name="")

  perfil_id = models.ForeignKey("Profile", verbose_name="Perfil", on_delete=models.CASCADE)
  area_id = models.ForeignKey("Area", verbose_name="Area", on_delete=models.CASCADE)
  dep_id = models.ForeignKey("Department", verbose_name="Departamento", on_delete=models.CASCADE)
  position_id = models.ForeignKey("Position", verbose_name="Cargo", on_delete=models.CASCADE)

  contact_id = models.ForeignKey("ContactEmergency", verbose_name="Contacto de emergencia", null=True, on_delete=models.CASCADE)
  liability_id = models.ForeignKey("Liability", verbose_name="Carga", null=True, on_delete=models.CASCADE)

  def __str__(self):
    #row = "Rut: " + self.employee_rut + " - " + "Nombres: " + self.employee_firstname + " - " + "Apellidos: " + self.employee_lastname + " - " + "Dirección: " + self.employee_address + " - " + "Teléfono: " + self.employee_phone + " - " +  "Fecha ingreso: "
    return self.employee_firstname


class Profile(models.Model):
  perfil_id = models.AutoField(primary_key=True)
  perfil_name = models.CharField(max_length=30, verbose_name="Nombre Perfil", null=True)

  def __str__(self):
      return self.perfil_name
  

class Area(models.Model):
  area_id = models.AutoField(primary_key=True)
  area_name = models.CharField(max_length=30, verbose_name="Nombre Area", null=True)

  def __str__(self):
      return self.area_name
  

class Department(models.Model):
  dep_id = models.AutoField(primary_key=True)
  dep_name = models.CharField(max_length=30, verbose_name="Nombre Departamento", null=True)

  area_id = models.ForeignKey("Area", verbose_name=("Area"), null=True, on_delete=models.CASCADE)

  def __str__(self):
      return self.dep_name
  

class Position(models.Model):
  position_id = models.AutoField(primary_key=True)
  position_name = models.CharField(max_length=30, verbose_name="Nombre Cargo", null=True)

  dep_id = models.ForeignKey("Department", verbose_name=("Departamento"), null=True, on_delete=models.CASCADE)

  def __str__(self):
      return self.position_name
  

class ContactEmergency(models.Model):  
  contact_id = models.AutoField(primary_key=True)
  contact_relation = models.CharField(max_length=50, verbose_name="Relación Parentesca Contacto de emergencia", null=True)
  contact_phone = models.CharField(max_length=30, verbose_name="Teléfono Contacto de emergencia", null=True)
  contact_firstname = models.CharField(max_length=50, verbose_name="Nombres Contacto de emergencia", null=True)
  contact_lastname = models.CharField(max_length=50, verbose_name="Apellidos Contacto de emergencia", null=True)

  employee_rut = models.ForeignKey("Employee", verbose_name=(""), null=True, on_delete=models.CASCADE)

  def __str__(self):
    row = "Parentesco: " + self.contact_relation + " - " + "Nombres: " + self.contact_firstname + " - " + "Apellidos: " + self.contact_lastname + " - " + "Teléfono: " + self.contact_phone
    return row


class Liability(models.Model):  

   #
  select_gender = (
    ('M', "Masculino"),
    ('F', "Femenino")
  )

  liability_id = models.AutoField(primary_key=True)
  liability_rut = models.CharField(max_length=50, verbose_name="Rut Carga", null=True)
  liability_firstname = models.CharField(max_length=60, verbose_name="Nombre Carga", null=True)
  liability_lastname = models.CharField(max_length=50, verbose_name="Apellido Carga", null=True)  
  liability_gender = models.CharField(max_length=1, verbose_name="Género Carga", null=True, choices=select_gender, default='')
  liability_kin = models.CharField(max_length=50, verbose_name="Parentesco Carga", null=True)

  employee_rut = models.ForeignKey("Employee", verbose_name=("Rut trabajador"), null=True, on_delete=models.CASCADE)

  def __str__(self):
    row = "Rut carga: " + self.liability_rut + " - " + "Nombres: " + self.liability_firstname + " - " + "Apellidos: " + self.liability_lastname + " - " + "Parentesco carga: " + self.liability_kin + " - " + "Género: " + self.liability_gender
    return row