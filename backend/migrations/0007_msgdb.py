# Generated by Django 4.1.3 on 2023-02-13 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_remove_serdetails_sertp'),
    ]

    operations = [
        migrations.CreateModel(
            name='msgdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('mail', models.EmailField(blank=True, max_length=100, null=True)),
                ('sub', models.CharField(blank=True, max_length=100, null=True)),
                ('messge', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
