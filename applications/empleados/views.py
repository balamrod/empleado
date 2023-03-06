from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import (    
    ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
)

#models
from .models import Empleado

class InicioView(TemplateView):
    """ vista que carga la pagina de inicio"""
    template_name = 'inicio.html'

class ListAllEMpleados(ListView):
    template_name ='empleados/list_all.html'
    paginate_by = 4
    ordering = 'id'
    context_object_name ='empleados'

    def get_queryset(self):   
        palabra_clave = self.request.GET.get("kword",'')   
        
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave
        )
        return lista

class ListaEmpleadosAdmin(ListView):
    template_name ='empleados/lista_empleados.html'
    paginate_by = 10
    ordering = 'id'
    context_object_name ='empleados'
    model = Empleado

class ListByAreaEmpleado(ListView):
    template_name ='empleados/list_by_area.html'

    def get_queryset(self):
        area = self.kwargs['name']
        lista = Empleado.objects.filter(
            departamento__name=area
        )
        return lista

class ListEmpleadosByKword(ListView):
    # lista empleado por palabra clave
    template_name = 'empleados/by_kword.html'
    context_object_name ='empleados'

    def get_queryset(self):   
        print('******************')
        palabra_clave = self.request.GET.get("kword",'')   
        print('========',palabra_clave)
        
        lista = Empleado.objects.filter(
            first_name=palabra_clave
        )
        return lista

class ListaHabilidadesEmpleado(ListView):
    template_name = 'empleados/habilidades.html'
    context_object_name ='habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=1)
        return empleado.habilidades.all()


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "empleados/detalle_empleado.html"
 
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'empleado del mes'
        return context


class SuccessView(TemplateView):
    template_name = "empleados/success.html"


class EmpleadoCreateView(CreateView):
    template_name = "empleados/add.html"
    model = Empleado
    fields=['first_name','last_name','job','departamento','habilidades','avatar']    
    success_url = reverse_lazy('persona_app:empleados_admin')
    #fields=('__all__')
    #success_url = '/success'
    #success_url = '.' para rediccionar a la misma página

    def form_valid(self, form):
        #logica del proceso
        empleado = form.save(commit=False) #el commit solo guarda en una variable y luego se guarda en el siguiente save()
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView,self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "empleados/update.html"
    fields=['last_name','first_name','job','departamento','habilidades']
    success_url = reverse_lazy('persona_app:empleados_admin')

    #guardar datos antes de ser validados por el formulario
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request,*args, **kwargs)

    def form_valid(self, form):
        return super(EmpleadoUpdateView,self).form_valid(form)

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "empleados/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')


    