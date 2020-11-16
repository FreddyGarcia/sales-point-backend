import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class GeneralManager(models.Manager):
    def get_queryset(self):
        return super(GeneralManager, self).get_queryset().filter(is_enabled=True)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_enabled = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='%(class)s_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='%(class)s_updated_by')

    objects = models.Manager()
    api_objects = GeneralManager()

    def from_request(self, request):
        self.created_by = request.user
        self.updated_by = request.user
        return self

    def delete(self):
        # do not delete the instance, only disable it
        self.is_enabled = False
        self.save()

    class Meta:
        abstract = True


class CompanyGroup(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Company(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    group = models.ForeignKey(CompanyGroup, on_delete=models.PROTECT)
    user = models.ManyToManyField('UserProfile')
    economic_activity = models.ForeignKey('EconomicActivity', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"


class BaseModelCompany(BaseModel):

    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    class Meta:
        abstract = True


class EconomicActivity(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Economic activity"
        verbose_name_plural = "Economic activities"


class Branch(BaseModelCompany):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"


class BranchAddress(BaseModelCompany):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    branch_address = models.OneToOneField(Branch, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.street} / {self.city}'

    class Meta:
        verbose_name = "Branch Address"
        verbose_name_plural = "Branches Address"


class ProductFamily(BaseModelCompany):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Product Family"
        verbose_name_plural = "Product Families"


class ProductLine(BaseModelCompany):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Product Line"
        verbose_name_plural = "Product Lines"


class ProductMeasureUnit(BaseModelCompany):
    description = models.CharField(max_length=100)
    symbol = models.CharField(max_length=5)
    unit_value = models.IntegerField()

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Measure Unit"
        verbose_name_plural = "Measure Units"


class Product(BaseModelCompany):
    description = models.CharField(max_length=200)
    barcode = models.CharField(max_length=50)
    family = models.ForeignKey(ProductFamily, on_delete=models.PROTECT)
    image = models.ForeignKey('MediaResource', on_delete=models.PROTECT)
    line = models.ForeignKey(ProductLine, on_delete=models.PROTECT)
    unit = models.ForeignKey(ProductMeasureUnit, on_delete=models.PROTECT)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='%(class)s_created_by', null=True)
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='%(class)s_updated_by', null=True)

    def __str__(self):
        return self.user.username


class MediaResource(BaseModelCompany):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.FileField(upload_to='resources')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()