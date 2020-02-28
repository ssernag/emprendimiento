from django.conf.urls import include, url
from GestionClientes.views import clienteregistroview, index

urlpatterns = [
  #url(r'$',clienteregistroview)
  url(r'$', index),
]
