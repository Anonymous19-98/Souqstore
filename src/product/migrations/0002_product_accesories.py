# Generated by Django 3.2 on 2021-05-03 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Accesories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ACCAlternatives', models.ManyToManyField(related_name='Accesories_prodects', to='product.Product')),
                ('ACCProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Main_Accesorie_prodect', to='product.product')),
            ],
            options={
                'verbose_name': 'Product Accesorie',
                'verbose_name_plural': 'Product Accesories',
            },
        ),
    ]
