# Generated by Django 5.0.4 on 2024-07-05 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_customer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
    ]
