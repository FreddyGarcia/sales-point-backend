from django.db import models
from apps.core.models import BaseModel
from apps.crm.models import Company

# Create your models here.


class Product(BaseModel):
    description = models.CharField(max_length=200)
    barcode = models.CharField(max_length=50)
    family = models.ForeignKey('ProductFamily', on_delete=models.PROTECT)
    image = models.ForeignKey('crm.MediaResource', on_delete=models.PROTECT)
    line = models.ForeignKey('ProductLine', on_delete=models.PROTECT)
    unit = models.ForeignKey('ProductMeasureUnit', on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class ProductFamily(BaseModel):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product Family"
        verbose_name_plural = "Product Families"


class ProductLine(BaseModel):
    description = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Product Line"
        verbose_name_plural = "Product Lines"


class ProductMeasureUnit(BaseModel):
    description = models.CharField(max_length=100)
    symbol = models.CharField(max_length=5)
    unit_value = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Measure Unit"
        verbose_name_plural = "Measure Units"
