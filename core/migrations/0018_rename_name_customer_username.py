# Generated by Django 5.0.4 on 2024-07-06 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_remove_customer_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='username',
        ),
    ]