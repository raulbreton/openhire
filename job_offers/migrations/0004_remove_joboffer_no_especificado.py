# Generated by Django 5.0.1 on 2024-02-12 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_offers', '0003_remove_joboffer_exterior_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joboffer',
            name='no_especificado',
        ),
    ]