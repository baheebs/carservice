# Generated by Django 4.1.3 on 2023-02-14 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_rename_quantity_serdetails_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serdetails',
            old_name='phone',
            new_name='Quantity',
        ),
    ]
