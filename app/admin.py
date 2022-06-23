from django.contrib import admin
from .models import Categoria, Producto, Contacto
# Register your models here.
from .forms import ProductoForm


class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "categoria"]
    list_editable = ["precio"]
    form = ProductoForm


admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto)
