from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Brand (models.Model):
    BRDName = models.CharField(max_length=255, verbose_name="Brand Name")
    BRSDesc = models.TextField(
        blank=True, null=True, verbose_name="Brand Description")

    class Meta():
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        return str(self.BRDName)


class Variant(models.Model):
    VARName = models.CharField(max_length=255, verbose_name="Variant Name")
    VARDesc = models.TextField(
        blank=True, null=True, verbose_name="Variant Description")

    class Meta():
        verbose_name = _("Variant")
        verbose_name_plural = _("Variants")

    def __str__(self):
        return str(self.VARName)
