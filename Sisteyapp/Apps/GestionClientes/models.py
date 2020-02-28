from django.db import models

# Create your models here.
class Cliente(models.Model):
    PrimerApellido = models.CharField(max_length=35)
    SegundoApellido = models.CharField(max_length=35)
    Nombres = models.CharField(max_length=35)
    CedulaCiudadania = models.CharField(max_length=12)
    FechaNacimiento = models.DateField()
    SEXOS = (('F', 'Femenino'), ('M', 'Masculino'))
    Sexo = models.CharField(max_length=1, choices=SEXOS, default='M')
    CorreoElectronico = models.EmailField()
    FechaExpedicionCedula = models.DateField()
    TelefonoContacto = models.CharField(max_length=14, help_text="Ingresa número de contacto")
    DireccionResidencia = models.CharField(max_length=40)
    Ciudad = models.CharField(max_length=60)
    Departamento = models.CharField(max_length=30)
    Pais = models.CharField(max_length=50)
    ReferenciaPersonal =models.CharField(max_length=50)
    TelefonoReferencia = models.CharField(max_length=14, help_text="Ingresa número de contacto")

    def NombreCompleto(self):
        cadena = "{0} {1}, {2}"
        return  cadena.format(self.PrimerApellido, self.SegundoApellido, self.Nombres)

    def __str__(self):
       return self.NombreCompleto()

class TipoCredito (models.Model):
    Nombre = models.CharField(max_length=50)
    Rango = models.PositiveSmallIntegerField()
    ESTADOS = (('A', 'Aprobado'), ('P', 'Pendiente'), ('R', 'Rechazado'), ('T','Trámite') )
    Estado = models.CharField(max_length=1, choices=ESTADOS)

    def __str__(self) :
       return "{0}".format(self.Nombre)

class Credito (models.Model):
    Cliente = models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE)
    TipoCredito = models.ForeignKey(TipoCredito, null=False, blank=False, on_delete=models.CASCADE)
    FechaSolicitud = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        cadena = "{0} => {1}"
        return cadena.format(self.Cliente, self.TipoCredito.Nombre)
