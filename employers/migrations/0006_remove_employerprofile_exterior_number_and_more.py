# Generated by Django 5.0.2 on 2024-03-04 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0005_alter_employerprofile_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employerprofile',
            name='exterior_number',
        ),
        migrations.RemoveField(
            model_name='employerprofile',
            name='interior_number',
        ),
        migrations.RemoveField(
            model_name='employerprofile',
            name='municipality',
        ),
    ]