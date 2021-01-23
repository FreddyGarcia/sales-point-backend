from django.contrib.admin import ModelAdmin, TabularInline, site
from .models import *
from apps.core.admin import BaseModelAdmin
from django.forms.models import BaseInlineFormSet



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
    readonly_fields = tuple(set(BaseModelAdmin.readonly_fields) - set(('company',)))


class CompanyModelAdmin(BaseModelAdmin):
    readonly_fields = tuple(set(BaseModelAdmin.readonly_fields) - set(('company',)))


class MediaResourceModelAdmin(BaseModelAdmin):
    readonly_fields = tuple(set(BaseModelAdmin.readonly_fields) - set(('company',)))


site.register(CompanyGroup, CompanyModelAdmin)
site.register(EconomicActivity, CompanyModelAdmin)
site.register(Company, CompanyModelAdmin)
site.register(Branch, BranchAdmin)
site.register(MediaResource, MediaResourceModelAdmin)
