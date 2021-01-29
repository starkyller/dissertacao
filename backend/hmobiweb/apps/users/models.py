import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class ContactType(models.Model):
    name = models.CharField(_('Contact Type Name'), max_length=50, unique=True, help_text=_(
        "Add a name for a type of contact, e.i, phone number, WeChat"),)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Contact Type")
        verbose_name_plural = _("Contact Types")


class Contact(models.Model):
    contact_type = models.ForeignKey('ContactType', on_delete=models.CASCADE,)
    user = models.ForeignKey('User', on_delete=models.CASCADE,)

    value = models.CharField(max_length=200, unique=True, blank=False, help_text=_(
        "Add a value for a contact, e.i, phone number or Wechat ID or email"),)

    def __str__(self):
        return _("Contact of type: %s") % self.contact_type.name

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")


class Guardian(models.Model):
    user_target = models.OneToOneField('User', on_delete=models.CASCADE)
    user_guardians = models.ManyToManyField(
        'User', blank=True, related_name='+')

    def __str__(self):
         # Translators: e.i Guardians of: john123
        return _("Guardians of: %s") % self.user_target.username

    class Meta:
        verbose_name = _("Guardian")
        verbose_name_plural = _("Guardians")


class User(AbstractUser):
    '''
        My custom user model
    '''
    class Types(models.TextChoices):
        PATIENT = "PATIENT", _('Patient')
        MEDICALSTAFF = "MEDICALSTAFF", _('Medical Staff')

    base_type = Types.PATIENT

    type = models.CharField(_('Type of User'), max_length=50,
                            choices=Types.choices, default=Types.PATIENT,)

    alias = models.UUIDField(
        default=uuid.uuid4, editable=False, db_index=True,)

    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.base_type
        return super().save(*args, **kwargs)

    @property
    def contacts(self):
        return self.contacts

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")


class PatientManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.PATIENT)


class MedicalStaffManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.MEDICALSTAFF)


class MedicalStaff(User):

    base_type = User.Types.MEDICALSTAFF

    objects = MedicalStaffManager()

    class Meta:
        proxy = True


class Patient(User):

    base_type = User.Types.PATIENT

    objects = PatientManager()

    @property
    def guardians(self):
        """returns the user guardians"""
        return self.guardian.user_guardians.all()

    @property
    def guardian_of(self):
        """returns the the patients that the patient is guardian of"""
        qs = Guardian.objects.filter(user_guardians__in=[self.id])
        qs_list = list(qs)
        objs = []

        for x in qs_list:
            objs.append(x.user_target.id)
        

        return User.objects.filter(pk__in=objs)

    class Meta:
        proxy = True
