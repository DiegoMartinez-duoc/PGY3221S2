from django.db import models

# Create your models here.

class Rol(models.Model):
    rol_id = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nombre_rol

class ThreadUser(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=24)
    nombre_usuario = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre_usuario

class CredencialesUsuario(models.Model):
    usuario = models.OneToOneField(
        ThreadUser,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='credenciales'
    )
    email = models.EmailField(max_length=255, unique=True)
    contrasena = models.CharField(max_length=128)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return self.email

class Seguidor(models.Model):
    seguidor = models.ForeignKey(
        ThreadUser,
        on_delete=models.CASCADE,
        related_name='siguiendo'
    )
    seguido = models.ForeignKey(
        ThreadUser,
        on_delete=models.CASCADE,
        related_name='seguidores'
    )
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('seguidor', 'seguido')

    def __str__(self):
        return f"{self.seguidor} sigue a {self.seguido}"

class Thread(models.Model):
    thread_id = models.AutoField(primary_key=True)
    nombre_thread = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='threads/', null=True, blank=True)
    mensaje = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    usuario = models.ForeignKey(
        ThreadUser,
        on_delete=models.CASCADE,
        related_name='threads'
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_thread

class Comentario(models.Model):
    comentario_id = models.AutoField(primary_key=True)
    mensaje = models.TextField()
    usuario = models.ForeignKey(
        ThreadUser,
        on_delete=models.CASCADE,
        related_name='comentarios'
    )
    thread = models.ForeignKey(
        Thread,
        on_delete=models.CASCADE,
        related_name='comentarios'
    )
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.usuario} en {self.thread}"