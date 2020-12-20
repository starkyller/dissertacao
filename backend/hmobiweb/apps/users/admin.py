from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

from .models import Contact, ContactType

User = get_user_model()



class ContactTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]



class InLineContact(admin.TabularInline):
    model = Contact
    extra = 1

#@admin.register(User)
class UserAdmin(UserAdmin):
    inlines = [InLineContact]

    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    #list_display = ['pk', 'email', 'username', 'first_name', 'last_name']
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Stuff", {'fields': ('email', 'first_name', 'type',)}),
    )
    fieldsets = UserAdmin.fieldsets
    
    list_display = ["username", "alias", "is_superuser"]
    search_fields = ["username", "alias"]

admin.site.register(User, UserAdmin)
admin.site.register(ContactType, ContactTypeAdmin)