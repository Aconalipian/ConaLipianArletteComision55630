from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy


#se importa todos los modelos de models.py
from .models import *
#se importa todos los formularios de forms.py
from .forms import *


#estas vistas para crear funcionalidad con class based views CBV
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from .forms import MiModeloForm

#esta libreria es para trabajar con autenticación, formulario que ya viene con django
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth  import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def Home(request):
    return render(request, "app/home.html")

def About(request):
    return render(request, "app/about.html")




#Acá se define cada formulario por modelo
def buscarForm(request):
    return render(request, "app/buscar.html")

def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        peli = cpelicula.objects.filter(nombre__icontains=patron)
        contexto= {"peliculas":peli, 'titulo': f"Películas encontradas con patrón: {patron}"}
        return render(request,"app/pelicula.html", contexto)
    return HttpResponse("No ha ingresado nada, favor escriba un valor a buscar")




#______________________________ Login / Logout y Registro ____________________________________________________

def login_request(request):    
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)
                return render(request, "app/base.html",{'mensaje':f'Bienvenido al sitio {usuario}'})
            else:
                return render(request, "app/login.html",{'form':miForm, 'mensaje':f'Los datos son inválidos...'})
        else:
             return render(request, "app/login.html",{'form':miForm, 'mensaje':f'Los datos son inválidos...'})  

    miForm = AuthenticationForm()
    return render(request, "app/login.html", {"form":miForm})


def registrar(request):
    if request.method == "POST":
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "app/base.html")
    else:
        miForm =   RegistroUsuariosForm()      
    return render(request, "app/registro.html", {"form":miForm}) 


#___________________________________editar perfil y avatar ___________________________________________


@login_required
def editaPerfil(request):
    usuario=request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request,"app/base.html")
        else:
            return render(request,"app/editarPerfil.html", {'form': form, 'usuario': usuario.username})
    else:
        form = UserEditForm(instance=usuario)
    return render(request,"app/editarPerfil.html",{'form': form, 'usuario': usuario.username} )



@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES) # Diferente a los forms tradicionales
        if form.is_valid():
            u = User.objects.get(username=request.user)

            # ____ Para borrar el avatar viejo
            avatarViejo = cAvatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

            # ____ Guardar el nuevo
            avatar = cAvatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            # ___ Hago que la url de la imagen viaje en el request
            imagen = cAvatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request,"app/base.html")
    else:
        form = AvatarFormulario()
    return render(request, "app/agregarAvatar.html", {'form': form })

        








#_________________________________________________class based views CBV__________________________________________________________

class directorList(LoginRequiredMixin, ListView):
    model = cdirector

class directorCreate(LoginRequiredMixin, CreateView):
    model = cdirector
    fields = ['nombre', 'nacionalidad']
    success_url = reverse_lazy('director')

class directorUpdate(LoginRequiredMixin, UpdateView):
    model = cdirector
    fields = ['nombre', 'nacionalidad']
    success_url = reverse_lazy('director')

class directorDelete(LoginRequiredMixin, DeleteView):
    model = cdirector
    success_url = reverse_lazy('director')





class peliculaList(LoginRequiredMixin, ListView):
    model = cpelicula
    
class peliculaCreate(LoginRequiredMixin,CreateView):
    model = cpelicula
    form_class = MiModeloForm
    ##fields = ['nombre', 'fecha_estreno', 'productora','genero']
    success_url = reverse_lazy('pelicula')

class peliculaUpdate(LoginRequiredMixin, UpdateView):
    model = cpelicula
    fields = ['nombre', 'fecha_estreno', 'productora','genero']
    success_url = reverse_lazy('pelicula')

class peliculaDelete(LoginRequiredMixin, DeleteView):
    model = cpelicula
    success_url = reverse_lazy('pelicula')




class productoraList(LoginRequiredMixin,ListView):
    model = cproductora

class productoraCreate(LoginRequiredMixin, CreateView):
    model = cproductora
    fields = ['nombre', 'pais']
    success_url = reverse_lazy('productoras')

class productoraUpdate(LoginRequiredMixin, UpdateView):
    model = cproductora
    fields = ['nombre', 'pais']
    success_url = reverse_lazy('productoras')

class productoraDelete(LoginRequiredMixin, DeleteView):
    model = cproductora
    success_url = reverse_lazy('productoras')
