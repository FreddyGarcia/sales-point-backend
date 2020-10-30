from django.contrib import admin
from .models import *
# Register your models here.

class BaseModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()
        super().save_model(request, obj, form, change)

    readonly_fields=('created_by', 'updated_by')

admin.site.register(Company, BaseModelAdmin)
admin.site.register(Branch, BaseModelAdmin)
admin.site.register(BranchAddress, BaseModelAdmin)
admin.site.register(ProductFamily, BaseModelAdmin)
admin.site.register(ProductLine, BaseModelAdmin)
admin.site.register(ProductMeasureUnit, BaseModelAdmin)
admin.site.register(Product, BaseModelAdmin)
