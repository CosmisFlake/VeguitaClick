# Generated by Django 5.0.4 on 2024-07-03 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_carrier_weighttype_product_weight_product_tipo_peso'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]