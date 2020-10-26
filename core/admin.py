from django.contrib import admin
from .models import *
# Register your models here.

class BaseModelAdmin(admin.ModelAdmin):
      pass

admin.site.register(Company, BaseModelAdmin)
admin.site.register(Branch, BaseModelAdmin)
admin.site.register(ProductFamily, BaseModelAdmin)
admin.site.register(ProductLine, BaseModelAdmin)
admin.site.register(ProductMeasureUnit, BaseModelAdmin)
admin.site.register(Product, BaseModelAdmin)
