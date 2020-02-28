from django.conf.urls import include, url
from GestionClientes.views import clienteregistroview,index


urlpatterns = [
  url(r'nuevo$',clienteregistroview, name = 'registro'),
  #url(r'$', principal),
  url(r'$', index),
]
