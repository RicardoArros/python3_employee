from django import forms
from .models import Employee
from .models import ContactEmergency


class EmployeeForm(forms.ModelForm):
  class Meta:
    model = Employee
    # fields = '__all__'  
    fields = ['employee_rut', 'employee_firstname', 'employee_lastname', 'employee_address', 
    'employee_phone', 'employee_gender', 'employee_companyDate', 'perfil_id', 'area_id', 
    'dep_id', 'position_id', 'contact_id', 'liability_id']
    widgets = {
      'employee_companyDate': forms.DateInput(attrs={'type': 'date'})
    }

  
  def __init__(self, *args, **kwargs):
    # initialize form, which will create self.fields dict
    super(EmployeeForm, self).__init__(*args, **kwargs)
        
    self.fields['employee_rut'].widget.attrs.update({
      'class': 'mb-4',
    })

    self.fields['employee_firstname'].widget.attrs.update({
      'class': 'mb-4',
    })

    self.fields['employee_lastname'].widget.attrs.update({
      'class': 'mb-4',
    })

    self.fields['employee_address'].widget.attrs.update({
      'class': 'mb-4',
    })

    self.fields['employee_phone'].widget.attrs.update({
      'class': 'mb-4',
    })    

    self.fields['employee_gender'].widget.attrs.update({
      'class': 'mb-4',
    })

    self.fields['employee_companyDate'].widget.attrs.update({
      'class': 'mb-4',
    })

    # employee_companyDate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))



class ContactEmergencyForm(forms.ModelForm):
  class Meta:
    model = ContactEmergency
    fields = '__all__'  