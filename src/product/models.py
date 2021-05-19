from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

# Create your models here.


class Product(models.Model):
    PRDName = models.CharField(max_length=255, verbose_name=("Product Name"))
    PRDDesc = models.TextField(verbose_name=("Product Description"))
    PRDCategory = models.ForeignKey(
        'Category', on_delete=models.CASCADE, verbose_name=("Product Category"))
    PRDBrand = models.ForeignKey(
        'settings.Brand', on_delete=models.CASCADE, verbose_name=("Product Brand"), blank=True, null=True)
    PRDPrice = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name=("Product Price"))
    PRDCost = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name=("Product Cost"))
    PRDDiscount = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name=("Product Discount"), blank=True, null=True)
    PRDImage = models.ImageField(
        upload_to='product', verbose_name=("Product Image"), blank=True, null=True)
    PRDCreatedAt = models.DateTimeField(
        max_length=255, verbose_name=("Created At"))
    PRDSlug = models.SlugField(blank=True, null=True)

    class Meta():
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def save(self, *args, **kwargs):
        if not self.PRDSlug:
            self.PRDSlug = slugify(self.PRDName)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.PRDName


class Category(models.Model):
    CATName = models.CharField(max_length=255, verbose_name=("Category Name"))
    CATSub_Category = models.ForeignKey('self', limit_choices_to={
                                        'CATSub_Category__isnull': True}, on_delete=models.CASCADE, blank=True, null=True, verbose_name=("Category Sub-Category"))
    CATDesc = models.TextField(verbose_name=("Category Description"))
    CATImg = models.ImageField(
        upload_to='category', verbose_name=("Category Image"))
    CATCreatedAt = models.DateTimeField(
        max_length=255, verbose_name=("Created At"), blank=True, null=True)

    class Meta():
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.CATName


class Product_Alternative(models.Model):
    PALProduct = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="Main_prodect", verbose_name=("Product"))
    PALAlternatives = models.ManyToManyField(
        Product, related_name="Alternative_prodects", verbose_name=("Alternatives"))

    class Meta():
        verbose_name = _("Product Alternative")
        verbose_name_plural = _("Product Alternatives")

    def __str__(self):
        return str(self.PALProduct)


class Product_Accesories(models.Model):
    ACCProduct = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="Main_Accesorie_prodect", verbose_name=("Product"))
    ACCAlternatives = models.ManyToManyField(
        Product, related_name="Accesories_prodects", verbose_name=("Accesories"))

    class Meta():
        verbose_name = _("Product Accesorie")
        verbose_name_plural = _("Product Accesories")

    def __str__(self):
        return str(self.ACCProduct)
