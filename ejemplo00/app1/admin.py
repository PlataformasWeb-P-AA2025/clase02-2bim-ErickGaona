from django.contrib import admin

from app1.models import Estudiante
from app1.models import Ciudad
admin.site.register(Ciudad)
admin.site.register(Estudiante)
