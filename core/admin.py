from django.contrib.admin import ModelAdmin, TabularInline, site
from .models import *
from django.forms.models import BaseInlineFormSet


class BaseModelAdmin(ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()
        super().save_model(request, obj, form, change)

    readonly_fields = ('created_by', 'updated_by')


class BranchAddressFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        user_id = self.user.id
        kwargs['initial'] = [ {'created_by': user_id, 'updated_by': user_id}, ]
        super(BranchAddressFormSet, self).__init__(*args, **kwargs)


class BranchAddressInline(TabularInline):
    model = BranchAddress
    formset = BranchAddressFormSet

    def get_formset(self, request, obj=None, **kwargs):
       formset = super(BranchAddressInline, self).get_formset(request, obj, **kwargs)
       formset.user = request.user
       return formset



class BranchAdmin(BaseModelAdmin):
    inlines = [BranchAddressInline]



site.register(Company, BaseModelAdmin)
site.register(Branch, BranchAdmin)
site.register(ProductFamily, BaseModelAdmin)
site.register(ProductLine, BaseModelAdmin)
site.register(ProductMeasureUnit, BaseModelAdmin)
site.register(Product, BaseModelAdmin)
site.register(EconomicActivity, BaseModelAdmin)
