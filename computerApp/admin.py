from django.contrib import admin

from .models import Machine
from .models import Utilisateur

admin.site.register(Machine)
admin.site.register(Utilisateur)

# Register your models here.
