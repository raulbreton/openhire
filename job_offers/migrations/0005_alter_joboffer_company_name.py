# Generated by Django 5.0.1 on 2024-02-14 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_offers', '0004_remove_joboffer_no_especificado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joboffer',
            name='company_name',
            field=models.CharField(max_length=100),
        ),
    ]