# Generated by Django 2.2 on 2019-04-30 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_shop_currency_iso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_link',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterModelTable(
            name='product',
            table='SH_Products',
        ),
    ]
