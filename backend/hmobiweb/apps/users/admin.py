from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as djUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext, gettext_lazy as _

from .models import Contact, ContactType, Guardian

User = get_user_model()


class ContactTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]


class InLineContact(admin.TabularInline):
    model = Contact
    extra = 1


class InLineGuardian(admin.TabularInline):
    model = Guardian
    extra = 1


class UserAdmin(djUserAdmin):
    inlines = [InLineContact, InLineGuardian]

    add_form = UserCreationForm
    form = UserChangeForm
    model = User

    fks = (
        (None, {'fields': ('username', 'password1', 'password2', 'type')}),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name'),
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )

    fksChange = (
        (None, {'fields': ('username', 'password', 'type')}),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name'),
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )

    add_fieldsets = fks
    fieldsets = fksChange

    list_display = ["username", "alias", "is_superuser"]
    search_fields = ["username", "alias"]

    class Media:
        js = ('users/admin/js/toggle_guardians.js',)


admin.site.register(User, UserAdmin)
admin.site.register(ContactType, ContactTypeAdmin)
