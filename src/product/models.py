from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    PRDName = models.CharField(max_length=255, verbose_name=_("Product Name"))
    PRDDesc = models.TextField(verbose_name=_("Product Description"))
    PRDCategory = models.ForeignKey(
        'Category', on_delete=models.CASCADE, verbose_name=_("Product Category"))
    PRDBrand = models.ForeignKey(
        'settings.Brand', on_delete=models.CASCADE, verbose_name=_("Product Brand"), blank=True, null=True)
    PRDPrice = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name=_("Product Price"))
    PRDCost = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name=_("Product Cost"))
    PRDDiscount = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name=_("Product Discount"), blank=True, null=True)
    PRDImage = models.ImageField(
        upload_to='product', verbose_name=_("Product Image"), blank=True, null=True)
    PRDCreatedAt = models.DateTimeField(
        max_length=255, verbose_name=_("Created At"))
    PRDSlug = models.SlugField(
        blank=True, null=True, verbose_name=_("Product Slug"))
    PRDIsBestseller = models.BooleanField(
        default=False, verbose_name=_("Bestseller"))
    PRDIsNew = models.BooleanField(default=True, verbose_name=_("New"))

    def save(self, *args, **kwargs):
        if not self.PRDSlug:
            self.PRDSlug = slugify(self.PRDName)
        super(Product, self).save(*args, **kwargs)

    class Meta():
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def get_absolute_url(self):

        return reverse('products:product_details', kwargs={'slug': self.PRDSlug})

    def __str__(self):
        return self.PRDName


class Category(models.Model):
    CATName = models.CharField(max_length=255, verbose_name=_("Category Name"))
    CATSub_Category = models.ForeignKey('self', limit_choices_to={
                                        'CATSub_Category__isnull': True}, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("Category Sub-Category"))
    CATDesc = models.TextField(verbose_name=_("Category Description"))
    CATImg = models.ImageField(
        upload_to='category', verbose_name=_("Category Image"))
    CATCreatedAt = models.DateTimeField(
        max_length=255, verbose_name=_("Created At"), blank=True, null=True)

    class Meta():
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.CATName


class Product_Alternative(models.Model):
    PALProduct = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="Main_prodect", verbose_name=_("Product"))
    PALAlternatives = models.ManyToManyField(
        Product, related_name="Alternative_prodects", verbose_name=_("Alternatives"))

    class Meta():
        verbose_name = _("Product Alternative")
        verbose_name_plural = _("Product Alternatives")

    def __str__(self):
        return str(self.PALProduct)


class Product_Accesories(models.Model):
    ACCProduct = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="Main_Accesorie_prodect", verbose_name=_("Product"))
    ACCAlternatives = models.ManyToManyField(
        Product, related_name="Accesories_prodects", verbose_name=_("Accesories"))

    class Meta():
        verbose_name = _("Product Accesory")
        verbose_name_plural = _("Product Accesories")

    def __str__(self):
        return str(self.ACCProduct)
