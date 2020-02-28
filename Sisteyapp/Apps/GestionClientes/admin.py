from django.contrib import admin
from Sisteyapp.Apps.GestionClientes.models import *
# Register your models here.

admin.site.register(Cliente)
admin.site.register(TipoCredito)
admin.site.register(Credito)