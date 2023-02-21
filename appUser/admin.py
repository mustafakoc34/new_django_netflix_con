from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Profil)

@admin.register(Profil)
class ProfilList(admin.ModelAdmin):
    list_display = ("id","user","name")




