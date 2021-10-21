from django.contrib import admin

from apps.products.models import Producto


# Register your models here.
class ProductoAdmin (admin.ModelAdmin):
    list_display =('descripcion','fecha','cantidad')
    ordering =('descripcion','fecha','cantidad')
    search_fields =('descripcion','cantidad')

admin.site.register(Producto,ProductoAdmin)



