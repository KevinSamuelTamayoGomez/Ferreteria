from django.contrib import admin
from .models import *

admin.site.register(Categoria)
admin.site.register(Articulo)
admin.site.register(Proveedor)
admin.site.register(Marca)
admin.site.register(Venta)
admin.site.register(DetalleVenta)