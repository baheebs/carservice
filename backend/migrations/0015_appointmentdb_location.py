# Generated by Django 4.1.3 on 2023-02-16 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_appointmentdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentdb',
            name='LOCATION',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]