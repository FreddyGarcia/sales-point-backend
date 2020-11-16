from django.contrib.admin import ModelAdmin, TabularInline, site
from .models import *
from django.forms.models import BaseInlineFormSet


class BaseModelAdmin(ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user

        if hasattr(obj, 'company_id'):
            obj.company = request.user.userprofile.company_set.first()

        obj.save()
        super().save_model(request, obj, form, change)

    readonly_fields = ['created_by', 'updated_by', 'company']


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


class CompanyModelAdmin(BaseModelAdmin):
    readonly_fields = tuple(set(BaseModelAdmin.readonly_fields) - set(('company',)))


class UserProfileModelAdmin(BaseModelAdmin):
    readonly_fields = ['created_by', 'updated_by', 'user']


site.register(UserProfile, UserProfileModelAdmin)
site.register(CompanyGroup, CompanyModelAdmin)
site.register(EconomicActivity, CompanyModelAdmin)
site.register(Company, CompanyModelAdmin)
site.register(Branch, BranchAdmin)
site.register(ProductFamily, BaseModelAdmin)
site.register(ProductLine, BaseModelAdmin)
site.register(ProductMeasureUnit, BaseModelAdmin)
site.register(Product, BaseModelAdmin)
site.register(MediaResource, BaseModelAdmin)
