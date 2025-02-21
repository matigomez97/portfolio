from django.contrib import admin
from .models import Proyecto, Habilidad, Educacion, Experiencia, Testimonio, MensajeContacto

admin.site.register(Proyecto)
admin.site.register(Habilidad)
admin.site.register(Educacion)
admin.site.register(Experiencia)
admin.site.register(Testimonio)
admin.site.register(MensajeContacto)
