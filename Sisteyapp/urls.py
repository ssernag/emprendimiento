from django.contrib import admin
from django.conf.urls import include, url
from GestionClientes.views import clienteregistroview


urlpatterns = [
  url(r'^admin/', admin.site.urls),
  #url(r'^nuevo/', clienteregistroview),
  url(r'^clientes/', include ('GestionClientes.urls')),
  #url(r'$', principal),
  ]
