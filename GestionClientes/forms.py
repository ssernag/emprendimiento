from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
           'PrimerApellido',
           'SegundoApellido',
           'Nombres',
           'CedulaCiudadania',
           'FechaNacimiento',
           'Sexo',
           'CorreoElectronico',
           'FechaExpedicionCedula',
           'TelefonoContacto',
           'DireccionResidencia',
           'Ciudad',
           'Departamento',
           'Pais',
           'ReferenciaPersonal',
           'TelefonoReferencia'
        ]
        labels = {

           'PrimerApellido': 'Primer Apellido',
           'SegundoApellido': 'Segundo Apellido',
           'Nombres' : 'Nombres',
           'CedulaCiudadania': 'Cédula de ciudadanía',
           'FechaNacimiento': 'Fecha de Nacimiento',
           'Sexo': 'Sexo',
           'CorreoElectronico': 'Correo Electronico',
           'FechaExpedicionCe:dula': 'Fecha de expedición de la cédula',
           'TelefonoContacto': 'Telefono de Contacto',
           'DireccionResidencia':'Direccion de Residencia',
           'Ciudad': 'Ciudad',
           'Departamento':'Departamento',
           'Pais': 'Pais',
           'ReferenciaPersonal': 'Referencia Personal',
           'TelefonoReferencia': 'Telefono de Referencia Personal'
        }