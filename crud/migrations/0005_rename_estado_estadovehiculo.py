# Generated by Django 5.0.6 on 2024-06-20 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_estado_tipovehiculo_transportista_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Estado',
            new_name='EstadoVehiculo',
        ),
    ]