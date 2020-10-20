import uuid
from django.db import models
from django.utils import timezone


# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(BaseModel, self).save(*args, **kwargs)

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
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"


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
    image_url = models.URLField(blank=True)

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
    image_url = models.URLField()
    unit = models.ForeignKey(ProductMeasureUnit, on_delete=models.PROTECT)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
