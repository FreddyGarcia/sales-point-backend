from django.contrib import admin
from .models import *
from apps.core.admin import BaseModelAdmin


class CustomModelAdmin(BaseModelAdmin):
    readonly_fields = tuple(set(BaseModelAdmin.readonly_fields))


# Register your models here.
admin.site.register(ProductFamily, CustomModelAdmin)
admin.site.register(ProductLine, CustomModelAdmin)
admin.site.register(ProductMeasureUnit, CustomModelAdmin)
admin.site.register(Product, CustomModelAdmin)
