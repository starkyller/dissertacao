from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin as djUserAdmin
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#from django.contrib.auth import get_user_model
from django.utils.translation import gettext, gettext_lazy as _

from .models import MonitoringCategory, SolutionObjective, Solution


class MonitoringCategoryAdmin(admin.ModelAdmin):
    model = MonitoringCategory

class SolutionObjectiveAdmin(admin.ModelAdmin):
    model = SolutionObjective

class SolutionAdmin(admin.ModelAdmin):
    model = Solution

admin.site.register(MonitoringCategory, MonitoringCategoryAdmin)
admin.site.register(SolutionObjective, SolutionObjectiveAdmin)
admin.site.register(Solution, SolutionAdmin)

# User = get_user_model()


# class ContactTypeAdmin(admin.ModelAdmin):
#     list_display = ["name"]


# class InLineContact(admin.TabularInline):
#     model = Contact
#     extra = 1


# class InLineGuardian(admin.TabularInline):
#     model = Guardian
#     extra = 1


# class UserAdmin(djUserAdmin):
#     inlines = [InLineContact, InLineGuardian]

#     add_form = UserCreationForm
#     form = UserChangeForm
#     model = User

#     fks = (
#         (None, {'fields': ('username', 'password')}),
#         (_('Personal info'), {
#             'fields': ('first_name', 'last_name', 'type'),
#         }),
#         (_('Permissions'), {
#             'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
#         }),
#     )

#     add_fieldsets = fks
#     fieldsets = fks

#     list_display = ["username", "alias", "is_superuser"]
#     search_fields = ["username", "alias"]

#     class Media:
#         js = ('users/admin/js/toggle_guardians.js',)


# admin.site.register(User, UserAdmin)
# admin.site.register(ContactType, ContactTypeAdmin)
