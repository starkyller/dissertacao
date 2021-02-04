from django.contrib import admin
from django.utils.translation import gettext, gettext_lazy as _


from .forms import SolutionForm
from .models import MonitoringCategory, SolutionObjective, Solution


class MonitoringCategoryAdmin(admin.ModelAdmin):
    model = MonitoringCategory

class SolutionObjectiveAdmin(admin.ModelAdmin):
    model = SolutionObjective

class SolutionAdmin(admin.ModelAdmin):
    model = Solution
    form = SolutionForm

    list_display = ["name", "category", "objective"]
    search_fields = ["name"]

    list_filter = ('category', 'objective')


admin.site.register(MonitoringCategory, MonitoringCategoryAdmin)
admin.site.register(SolutionObjective, SolutionObjectiveAdmin)
admin.site.register(Solution, SolutionAdmin)
