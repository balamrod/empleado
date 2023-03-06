from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .forms import PruebaForm

from .models import Prueba
# Create your views here.

class IndexView(TemplateView):
    template_name = 'home/home.html'

class PruebaListView(ListView):
    template_name = 'home/lista.html'
    queryset =  ['A','B','C']
    context_object_name = 'lista_pruebas'

class ModeloPruebaListView(ListView):
    model = Prueba
    template_name = "home/pruebas.html"
    context_object_name = 'lista_prueba'


class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    form_class = PruebaForm
    success_url = '.'
