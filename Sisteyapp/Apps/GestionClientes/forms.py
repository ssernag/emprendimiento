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
