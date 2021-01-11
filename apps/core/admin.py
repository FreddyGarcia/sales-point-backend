from django.contrib.admin import ModelAdmin, TabularInline, site, StackedInline
from django.contrib.auth.models import Permission, User
from django.contrib.auth.admin import UserAdmin

from .models import *



class BaseModelAdmin(ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user

        if not request.user.is_superuser:
            if hasattr(obj, 'company_id'):
                obj.company = request.user.userprofile.company_set.first()

        obj.save()
        super().save_model(request, obj, form, change)

    readonly_fields = ['created_by', 'updated_by', 'company']



class ProfileInline(StackedInline):
    model = UserProfile
    verbose_name = 'Perfil de Usuario'
    verbose_name_plural = 'Perfiles de Usuario'
    extra = 0
    # min_num = 1
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'userprofile')

    inlines = (ProfileInline, )
    can_add = True




class UserProfileModelAdmin(BaseModelAdmin):
    readonly_fields = ['created_by', 'updated_by', 'user']


# site.register(UserProfile, UserProfileModelAdmin)
site.unregister(User)
site.register(User, CustomUserAdmin)
