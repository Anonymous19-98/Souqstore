# Generated by Django 3.2 on 2021-05-04 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_product_prdcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='PRDCategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Product Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDImage',
            field=models.ImageField(blank=True, null=True, upload_to='product', verbose_name='Product Image'),
        ),
    ]
