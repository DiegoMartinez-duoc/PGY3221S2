from django.core.management.base import BaseCommand
from django.utils import timezone
from core.models import Rol, ThreadUser, CredencialesUsuario, Seguidor, Thread, Comentario
from datetime import datetime, timedelta
from django.utils.timezone import make_aware

class Command(BaseCommand):
    help = 'Pobla la base de datos con datos iniciales'

    def handle(self, *args, **kwargs):
        self.stdout.write("Creando datos iniciales...")
        
        # 1. Crear Roles
        admin_rol = Rol.objects.create(
            rol_id = 2,
            nombre_rol='admin'
        )
        usuario_rol = Rol.objects.create(
            rol_id = 1,
            nombre_rol='usuario'
        )

        # 2. Crear Usuarios con IDs específicos
        juan = ThreadUser.objects.create(
            usuario_id=61,
            nombre='Juan Pérez',
            nombre_usuario='juanp',
            fecha_nacimiento=datetime(1990, 5, 15).date()
        )

        maria = ThreadUser.objects.create(
            usuario_id=62,
            nombre='María García',
            nombre_usuario='mariag',
            fecha_nacimiento=datetime(1985, 8, 22).date()
        )

        pedro = ThreadUser.objects.create(
            usuario_id=63,
            nombre='Pedro López',
            nombre_usuario='pedrol',
            fecha_nacimiento=datetime(1995, 2, 10).date()
        )

        # 3. Crear Credenciales
        CredencialesUsuario.objects.create(
            usuario=juan,
            email='juan@example.com',
            contrasena='pass123',
            rol=usuario_rol
        )

        CredencialesUsuario.objects.create(
            usuario=maria,
            email='maria@example.com',
            contrasena='securepass',
            rol=usuario_rol
        )

        CredencialesUsuario.objects.create(
            usuario=pedro,
            email='pedro@example.com',
            contrasena='mypassword',
            rol=usuario_rol
        )

        # 4. Crear Seguidores (corregido usando make_aware)
        Seguidor.objects.create(
            seguidor=juan,
            seguido=maria,
            fecha=make_aware(datetime(2024, 1, 15, 9, 30))
        )

        Seguidor.objects.create(
            seguidor=maria,
            seguido=pedro,
            fecha=make_aware(datetime(2024, 1, 16, 14, 45))
        )

        Seguidor.objects.create(
            seguidor=pedro,
            seguido=juan,
            fecha=make_aware(datetime(2024, 1, 17, 11, 20))
        )

        # 5. Crear Threads (corregido usando make_aware)
        thread1 = Thread.objects.create(
            thread_id=61,
            nombre_thread='Primer Hilo',
            mensaje='Este es mi primer hilo en la plataforma',
            likes=15,
            usuario=juan,
            fecha_creacion=make_aware(datetime(2024, 1, 18, 10, 0))
        )

        thread2 = Thread.objects.create(
            thread_id=62,
            nombre_thread='Consejos Programación',
            mensaje='Comparto algunos consejos para nuevos programadores',
            imagen='threads/primer_hilo.jpg',
            likes=32,
            usuario=maria,
            fecha_creacion=make_aware(datetime(2024, 1, 19, 16, 30))
        )

        # 6. Crear Comentarios (corregido usando make_aware)
        Comentario.objects.create(
            comentario_id=61,
            mensaje='¡Bienvenido a la plataforma!',
            usuario=maria,
            thread=thread1,
            fecha=make_aware(datetime(2024, 1, 18, 10, 15))
        )

        Comentario.objects.create(
            comentario_id=62,
            mensaje='Gracias por los consejos, muy útiles',
            usuario=pedro,
            thread=thread2,
            fecha=make_aware(datetime(2024, 1, 19, 17, 0))
        )

        self.stdout.write(self.style.SUCCESS('Datos creados exitosamente!'))