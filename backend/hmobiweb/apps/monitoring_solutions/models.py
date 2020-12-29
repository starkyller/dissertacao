import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Slugable(models.Model):
    slug = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True,)

    class Meta:
        abstract = True


class MonitoringCategory(Slugable):
    designation = models.CharField(
        _('designation'), max_length=80, unique=True, help_text=_("E.i, Nutrition"),)

    def __str__(self):
        return self.designation

    class Meta:
        verbose_name = _("Monitoring Category")
        verbose_name_plural = _("Monitoring Categories")


class SolutionObjective(Slugable):
    designation = models.CharField(
        _('designation'), max_length=80, unique=True, help_text=_("E.i, Fall Detection"),)

    def __str__(self):
        return self.designation

    class Meta:
        verbose_name = _("Solution Objective")
        verbose_name_plural = _("Solutions Objectives")


class Solution(Slugable):
    category = models.ForeignKey('MonitoringCategory', verbose_name=_('Category'), on_delete=models.CASCADE, help_text=_(
        "The monitoring category to which the solution belongs"),)
    objective = models.ForeignKey('SolutionObjective', verbose_name=_('Objective'), on_delete=models.CASCADE, help_text=_(
        "The final objective of the solution in question"),)
    name = models.CharField(_('Name'), max_length=80,
                            unique=True, help_text=_("E.i, Fall Detection"),)
    description = models.CharField(_('Description'), max_length=350, blank=True, help_text=_(
        "Optional: Provide a description for your solution"),)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Solution")
        verbose_name_plural = _("Solutions")
