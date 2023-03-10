from django.contrib import admin
from .models import usuario, lugares

# Register your models here.

class AdminRegistrado(admin.ModelAdmin):
    list_display = ["__unicode__", "nombre"]
    class Meta:
        model =  usuario

admin.site.register(usuario, AdminRegistrado)
admin.site.register(lugares)