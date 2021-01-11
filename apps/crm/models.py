
from django.contrib.auth.models import User
from django.db import models
from apps.core.models import BaseModel
# Create your models here.

class CompanyGroup(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Company(BaseModel):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(CompanyGroup, on_delete=models.PROTECT)
    economic_activity = models.ForeignKey('EconomicActivity', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"



class EconomicActivity(BaseModel):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Economic activity"
        verbose_name_plural = "Economic activities"


class Branch(BaseModel):
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"


class BranchAddress(BaseModel):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.street} / {self.city}'

    class Meta:
        verbose_name = "Branch Address"
        verbose_name_plural = "Branches Address"


class MediaResource(BaseModel):
    content = models.FileField(upload_to='resources')
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.content)

