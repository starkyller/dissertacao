from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.users.models import Patient
from apps.monitoring_solutions.models import Solution


class UserSolutions(models.Model):
    patient = models.ForeignKey(Patient, verbose_name=_('Patient'), on_delete=models.CASCADE, help_text=_(
        "The patient to be associated with a specific solution"),)
    solution = models.ForeignKey(Solution, verbose_name=_('Solution'), on_delete=models.CASCADE, help_text=_(
        "The solution to be associated with a specific patient"),)

    class Meta:
        verbose_name = _("User Monitoring Solution")
        verbose_name_plural = _("User Monitoring Solutions")

        constraints = [
            models.UniqueConstraint(
                fields=['patient', 'solution'], name='patient to solution relation')
        ]


# class CollectedData(models.Model):
#     userSolution = models.ForeignKey(UserSolutions, verbose_name=_(
#         "User Solution"), on_delete=models.CASCADE, help_text=_("The User Solution that the collected data belongs to"),)
#     isValid = models.BooleanField(verbose_name=_(
#         "Is Valid"), blank=False, help_text=_("Is the sample valid?"),)
#     collectedTimeStamp = models.DateTimeField(verbose_name=_("Time Stamp of the collection"), blank=False, help_text=_(
#         "Time stamp at the time of collection of the data sample"),)

#     class Meta:
#         verbose_name = _("Collected Data")
#         verbose_name_plural = verbose_name