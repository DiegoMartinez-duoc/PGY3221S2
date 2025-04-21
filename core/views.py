from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UsuarioForm, CredencialesForm
from .models import ThreadUser, Rol, CredencialesUsuario, Seguidor, Thread, Comentario
import re

login = {
    'email': '',
    'nombre_usuario': '',
    'usuario_autenticado': False,
}

# Create your views here.
def home(request):

    login['threads'] = Thread.objects.all()


    return render(request, 'core/index.html', login)
    

def cerrar_sesion(request):
    login['usuario_autenticado'] = False
    login['email'] = ''
    login['nombre_usuario'] = ''
    login['credenciales'] = ''
    login['usuario'] = ''
    return redirect('home')
    
def login_completo(request):
    return render(request, 'core/login_completo.html')

def registro(request):
    return render(request, 'core/registro.html')

def inicio(request):
    
    context = {
                'error': False
            }
    return render(request, 'core/inicio.html', context)



def editar_cuenta(request):

    email = request.POST.get('email', '').strip()
 

    errores = []

    if not re.match(r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$', email):
        errores.append('Correo electrónico inválido')

    if errores:
        return render(request, 'core/micuenta.html', {
            'errores': errores,
            'mostrar_formulario': True  
        })


    usuario = login['usuario']
    credencial = login['credenciales']

    usuario.nombre = request.POST['nombre']
    usuario.nombre_usuario = request.POST['nombre_usuario']
    credencial.email = request.POST['email']
    credencial.contrasena = request.POST['contrasena']

    login['nombre_usuario'] = usuario.nombre_usuario
    login['email'] = credencial.email

    usuario.save()
    credencial.save()

    return render(request, 'core/micuenta.html', login)

def comentar(request):
    comentario = Comentario(
        mensaje=request.POST.get('comentario'),
        usuario=login['usuario'],
        thread=login['threads']
    )

    comentario.save()
    comentarios = Comentario.objects.filter(thread_id=login['threads'].thread_id)
    login['comentarios'] = comentarios


    return render(request, 'core/thread.html', login)

def ver_thread(request, id):

    if not login['usuario_autenticado']:
        return render(request, 'core/inicio.html')
    
    thread = get_object_or_404(Thread, thread_id=id)
    usuario_publicacion = get_object_or_404(ThreadUser, usuario_id = thread.usuario_id)
    comentarios = Comentario.objects.filter(thread_id=thread.thread_id)

    login['threads'] = thread
    login['comentarios'] = comentarios


    return render(request, 'core/thread.html', login)


def subir_thread(request):
    nuevo_thread = Thread(
        nombre_thread=request.POST.get('nombre_thread'),
        mensaje=request.POST.get('mensaje'),
        usuario=login['usuario']
    )
    
    if 'imagen' in request.FILES:
        nuevo_thread.imagen = request.FILES['imagen']
    
    nuevo_thread.save()

    thread = Thread.objects.filter(usuario_id = login['usuario'].usuario_id)
    login['threads'] = thread
   

    return render(request, 'core/hiloscreados.html', login)


def slider(request):
    if not login['usuario_autenticado']:
        return render(request, 'core/inicio.html')

    if (request.POST['url'] == 'crearHilo'):

        


        return render(request, 'core/crearhilo.html', login)
    
    elif (request.POST['url'] == 'hilosCreados'):

        thread = Thread.objects.filter(usuario_id = login['usuario'].usuario_id)
       

        login['threads'] = thread
       


        return render(request, 'core/hiloscreados.html', login)
    elif (request.POST['url'] == 'miCuenta'):
        return render(request, 'core/micuenta.html', login)
   

def enviarlogin(request):
    if request.method == 'POST':

        if (request.POST['email'] == 'admin' and request.POST['contrasena'] == 'admin'):

            usuario = ThreadUser.objects.all()
            thread = Thread.objects.all()

            context = {
                'usuarios': usuario,
                'threads': thread
            }


            return render(request, 'core/admin.html', context)


        

        try:
    
            credencial = CredencialesUsuario.objects.get(email=request.POST['email'])

            

            if credencial.contrasena == request.POST['contrasena']:
            
                    usuario = get_object_or_404(ThreadUser, pk=credencial.usuario_id)

                    rol = get_object_or_404(Rol, pk=credencial.rol_id)

                    if (rol.nombre_rol == 'admin'):
                        usuario = ThreadUser.objects.all()
                        thread = Thread.objects.all()

                        context = {
                            'usuarios': usuario,
                            'threads': thread
                        }

                        return render(request, 'core/admin.html', context)
                    

                    login['email'] = credencial.email
                    login['nombre_usuario'] = usuario.nombre_usuario
                    login['usuario_autenticado'] = True
                    login['usuario'] = usuario
                    login['credenciales'] = credencial

                    return render(request, 'core/login_completo.html')
        except CredencialesUsuario.DoesNotExist:
            context = {
                'error': True
            }
        

        return render(request, 'core/inicio.html', context)
    
def enviarregistro(request):
    if request.method == 'POST':

        errores = []

        if not re.match(r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$', request.POST['email']):
            errores.append(True)
        if request.POST['contrasena'] != request.POST['confirmar_contrasena']:
            errores.append(True)

        if errores:
            return render(request, 'core/registro.html', {
                'correo_error': errores[0],
                'contrasena_error': errores[1]  
            })


        formUsuario = UsuarioForm(request.POST)
        formCredenciales = CredencialesForm(request.POST)

        login['email'] = request.POST['email']
        login['nombre_usuario'] = request.POST['nombre_usuario']
        login['usuario_autenticado'] = True
        
      
        if formUsuario.is_valid():
            nuevo_usuario = formUsuario.save()
            cred = formCredenciales.save(commit=False)
            
            cred.usuario = nuevo_usuario

            login['usuario'] = nuevo_usuario
            login['credenciales'] = cred
            
            cred.save()
            redirect('home')
    else:
        formUsuario = UsuarioForm()
        formCredenciales = CredencialesForm()

    

    return render(request, 'core/login_completo.html', {'formUsuario': formUsuario, 'formCrendenciales': formCredenciales})


    
    


