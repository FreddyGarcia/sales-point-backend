import shortuuid
from abc import abstractmethod
from django.dispatch import receiver
from django.db.models.signals import post_save

from django.db import models
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel, SoftDeletableModel
from model_utils.managers import SoftDeletableManager

# Create your models here.
def get_unique_id():
    return shortuuid.random(length=24)


class BaseModel(TimeStampedModel, SoftDeletableModel, models.Model):
    unique_id = models.CharField(max_length=24, default=get_unique_id, editable=False, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='%(class)s_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='%(class)s_updated_by')

    objects = models.Manager()
    active = SoftDeletableManager()

    def from_request(self, request):
        self.created_by = request.user
        self.updated_by = request.user

        if hasattr(self, 'company_id'):
            company = Company.active.get(pk=request.auth.get('company'))
            self.company = company
        return self

    class Meta:
        abstract = True
        default_manager_name = 'active'

    @staticmethod
    @abstractmethod
    def get_reference_type():
        raise NotImplemented()

    @property
    def reference_code(self):
        if not self.pk:
            raise ValueError('Cannot get reference until object is saved')

        reference_number = str(self.pk).zfill(24)
        return f'{self.get_reference_type()}{reference_number}'


class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    created_by = models.OneToOneField(User, on_delete=models.PROTECT, related_name='%(class)s_created_by', null=True)
    updated_by = models.OneToOneField(User, on_delete=models.PROTECT, related_name='%(class)s_updated_by', null=True)
    branches = models.ManyToManyField('crm.Branch')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.userprofile.save()
    except Exception as identifier:
        pass
