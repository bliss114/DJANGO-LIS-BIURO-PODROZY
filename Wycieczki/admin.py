from django.contrib import admin

# Register your models here.
#from Biuro_podrozy.Wycieczki.models import Wycieczki
from .models import Wycieczki, Kategoria

admin.site.register(Wycieczki)
admin.site.register(Kategoria)