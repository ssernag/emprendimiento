from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
##from django.views.generic.base import TemplateView
from .forms import ClienteForm
from .models import Cliente
from django.http import HttpResponse

# Create your views here.
#def indexView(request):
    #return render(request,'index.html')

#@login_required
#def dashboardView(request):
    #return render(request,'principal.html')

def clienteregistroview(request):
    if request.method == 'POST':
     form = ClienteForm(request.POST)
     if form.is_valid():
               form.save()
     return redirect('index.html')
    else:
        form = ClienteForm()
    return render(request, 'nuevo/register.html',{'form': form})   

def index (request):
    return HttpResponse ('Index') 