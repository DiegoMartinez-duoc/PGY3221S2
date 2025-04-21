from django.urls import path
# from .views import (home, animales, armas, construcciones, 
#                     consumibles, enemigos, flora, forowiki, historia,
#                     inicio_sesion_wiki, logros, lugares, micuentatf, 
#                     recuperarcontra, registrarse_wiki, registro, inicio)
from .views import (home, registro, inicio, ver_thread, slider,
                    enviarregistro, enviarlogin, cerrar_sesion,
                    login_completo, editar_cuenta, subir_thread,
                    comentar)

urlpatterns = [
    path('', home, name="home"),
    path('registro/', registro, name="registro"),
    path('enviarregistro/', enviarregistro, name="enviarregistro"),
    path('inicio/', inicio, name="inicio"),
    path('enviarlogin/', enviarlogin, name="enviarlogin"),
    path('ver_thread/<int:id>/', ver_thread, name="ver_thread"),
    path('slider/', slider, name="slider"),
    path('cerrar_sesion/', cerrar_sesion, name="cerrar_sesion"),
    path('login_completo/', login_completo, name="login_completo"),
    path('editar_cuenta/', editar_cuenta, name="editar_cuenta"),
    path('subir_thread/', subir_thread, name="subir_thread"),
    path('comentar/', comentar, name="comentar"),
]