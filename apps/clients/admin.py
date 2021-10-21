from typing import List
from django.contrib import admin
from apps.clients.models import Cliente, ClienteProducto


# Register your models here.
class MembershipInline(admin.TabularInline):
    model = ClienteProducto
    extra =1


class ClienteAdmin (admin.ModelAdmin):
    inlines = (MembershipInline,)
    list_display =('nombre','fecha','cedula','casado')
    ordering =('nombre','fecha','cedula','casado')
    search_fields =('nombre','cedula')

admin.site.register(Cliente,ClienteAdmin)



