from django.contrib import admin
from .models import ThreadUser, Rol, CredencialesUsuario, Thread, Comentario, Seguidor

# Register your models here.
admin.site.register(ThreadUser)
admin.site.register(Rol)
admin.site.register(CredencialesUsuario)
admin.site.register(Thread)
admin.site.register(Comentario)
admin.site.register(Seguidor)