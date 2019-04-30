# Generated by Django 2.2 on 2019-04-30 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20190430_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cost_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='ratings',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]
