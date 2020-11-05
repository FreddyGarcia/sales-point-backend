import uuid
from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    filename = uuid.uuid4()
    return 'user_{0}/{1}'.format(instance.user.id, filename)

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

    def delete(self):
        # do not delete the instance, only disable it
        self.is_enabled = False
        self.save()

    class Meta:
        abstract = True


class Company(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"


class Branch(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"


class BranchAddress(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    branch_address = models.OneToOneField(Branch, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.street} / {self.city}'

    class Meta:
        verbose_name = "Branch Address"
        verbose_name_plural = "Branches Address"


class ProductFamily(BaseModel):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Product Family"
        verbose_name_plural = "Product Families"


class ProductLine(BaseModel):
    description = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Product Line"
        verbose_name_plural = "Product Lines"


class ProductMeasureUnit(BaseModel):
    description = models.CharField(max_length=100)
    symbol = models.CharField(max_length=5)
    unit_value = models.IntegerField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Measure Unit"
        verbose_name_plural = "Measure Units"


class Product(BaseModel):
    description = models.CharField(max_length=200)
    barcode = models.CharField(max_length=50)
    family = models.ForeignKey(ProductFamily, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='images/')
    unit = models.ForeignKey(ProductMeasureUnit, on_delete=models.PROTECT)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
