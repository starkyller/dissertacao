from django.contrib import admin

# Register your models here.
from django.utils.translation import gettext, gettext_lazy as _

from .models import UserSolutions


class UserSolutionsAdmin(admin.ModelAdmin):
    model = UserSolutions

    list_display = ["patient", "solution"]
    search_fields = ["patient",]

    list_filter = ('solution',)

    def has_change_permission(self, request, obj=None):
        # disable editing
        if obj is not None:
            return False
        return super().has_change_permission(request, obj=obj)


admin.site.register(UserSolutions, UserSolutionsAdmin)