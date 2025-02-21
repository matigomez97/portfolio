from django.db import models

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='proyectos/', null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Habilidad(models.Model):
    nombre = models.CharField(max_length=100)
    nivel = models.CharField(max_length=50, choices=[('Principiante', 'Principiante'), ('Intermedio', 'Intermedio'), ('Avanzado', 'Avanzado')])
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Educacion(models.Model):
    titulo = models.CharField(max_length=100)
    institucion = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} - {self.institucion}"

class Experiencia(models.Model):
    puesto = models.CharField(max_length=100)
    empresa = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.puesto} en {self.empresa}"

class Testimonio(models.Model):
    nombre = models.CharField(max_length=100)
    contenido = models.TextField()
    proyecto = models.ForeignKey(Proyecto, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Testimonio de {self.nombre}"

class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.nombre}"

