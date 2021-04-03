import json

from jsonschema import (
    validate,
    exceptions as jsonschema_exceptions
)

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

from apps.users.models import Patient
from apps.monitoring_solutions.models import Solution


class UserSolutions(models.Model):
    patient = models.ForeignKey(Patient, verbose_name=_('Patient'), on_delete=models.CASCADE, help_text=_(
        "The patient to be associated with a specific solution"),)
    solution = models.ForeignKey(Solution, verbose_name=_('Solution'), on_delete=models.CASCADE, help_text=_(
        "The solution to be associated with a specific patient"),)

    def __str__(self):
        return "%s - %s" % (self.patient.__str__(), self.solution.__str__())

    class Meta:
        verbose_name = _("User Monitoring Solution")
        verbose_name_plural = _("User Monitoring Solutions")

        constraints = [
            models.UniqueConstraint(
                fields=['patient', 'solution'], name='patient to solution relation')
        ]


class CollectedData(models.Model):
    userSolution = models.ForeignKey(UserSolutions, verbose_name=_(
        "User Solution"), blank=False, null=False, on_delete=models.CASCADE, help_text=_("The User Solution that the collected data belongs to"),)
    isValid = models.BooleanField(verbose_name=_(
        "Is Valid"), blank=False, help_text=_("Is the sample valid?"),)
    collectedTimeStamp = models.DateTimeField(verbose_name=_("Time Stamp of the collection"), blank=False, help_text=_(
        "Time stamp at the time of collection of the data sample"),)
    dataSample = models.JSONField(verbose_name=_("Data Sample"), blank=False, null=False, default=dict, help_text=_(
        "JSON Object that must fulfil the JSON Schema provided by the solution in question"),)

    def __str__(self):
        return self.userSolution.patient.__str__()

    def clean(self, *args, **kwargs):

        try:
            if self.dataSample is not None:
                _schema = self.userSolution.solution.sampleJsonSchema
                validate(instance=self.dataSample, schema=_schema)
        except jsonschema_exceptions.SchemaError as e:
            raise ValidationError(e.message, code='invalid')
        except jsonschema_exceptions.ValidationError as e:
            raise ValidationError({'dataSample': [e.message, ]})
        except Exception as e:
            raise ValidationError(e.message, code='invalid')

        super(CollectedData, self).clean(*args, **kwargs)

    class Meta:
        verbose_name = _("Collected Data")
        verbose_name_plural = verbose_name
