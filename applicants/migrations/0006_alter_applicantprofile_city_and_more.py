# Generated by Django 5.0.1 on 2024-02-21 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0005_alter_applicantprofile_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantprofile',
            name='city',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='applicantprofile',
            name='last_names',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='applicantprofile',
            name='state',
            field=models.CharField(max_length=255),
        ),
    ]
