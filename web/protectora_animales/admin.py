from django.contrib import admin
# Register your models here.

from .models import Protectora
from .models import Animal
from .models import Colaborador

admin.site.register(Protectora)
admin.site.register(Animal)
admin.site.register(Colaborador)
