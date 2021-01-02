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

    list_display = ["name", "category", "objective"]
    search_fields = ["name"]

    list_filter = ('category', 'objective')

admin.site.register(MonitoringCategory, MonitoringCategoryAdmin)
admin.site.register(SolutionObjective, SolutionObjectiveAdmin)
admin.site.register(Solution, SolutionAdmin)
