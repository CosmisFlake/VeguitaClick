# Generated by Django 5.0.6 on 2024-07-07 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0011_merge_20240706_2147'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipopeso',
            options={'ordering': ['id'], 'verbose_name': 'tipo de peso', 'verbose_name_plural': 'tipo de pesos'},
        ),
    ]
