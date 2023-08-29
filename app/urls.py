from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    
   path('', Home, name="home" ),
   path('about/', About, name="about" ),

   #formularios para guardar datos en el motor
   path('pelicula/', peliculaList.as_view(), name="pelicula" ),
   path('create_pelicula/', peliculaCreate.as_view(), name="create_pelicula" ),    
   path('update_pelicula/<int:pk>/', peliculaUpdate.as_view(), name="update_pelicula" ),
   path('delete_pelicula/<int:pk>/', peliculaDelete.as_view(), name="delete_pelicula" ),

   path('productoras/', productoraList.as_view(), name="productoras" ),
   path('create_productora/', productoraCreate.as_view(), name="create_productora" ),    
   path('update_productora/<int:pk>/', productoraUpdate.as_view(), name="update_productora" ),
   path('delete_productora/<int:pk>/', productoraDelete.as_view(), name="delete_productora" ),


   path('director/', directorList.as_view(), name="director" ),
   path('create_director/', directorCreate.as_view(), name="create_director" ),    
   path('update_director/<int:pk>/', directorUpdate.as_view(), name="update_director" ),
   path('delete_pdirector/<int:pk>/', directorDelete.as_view(), name="delete_director" ),




   # formulario de busqueda
   path('buscar/', buscarForm, name="buscar" ),
   path('buscar2/', buscar2, name="buscar2" ),

   # login y registro de usuario
   path('login/', login_request, name="login" ),
   path('logout/',LogoutView.as_view(template_name="app/logout.html") , name="logout" ),
   path('registrar/', registrar, name="registrar" ),

   # editar perfil y avatar
   path('edita_perfil/', editaPerfil, name="edita_perfil" ),
   path('agregar_avatar/', agregarAvatar, name="agregar_avatar" ),
   

   ]