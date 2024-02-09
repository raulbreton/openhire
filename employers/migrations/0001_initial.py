# Generated by Django 5.0.1 on 2024-02-09 01:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(default='None', max_length=100)),
                ('state', models.CharField(default='None', max_length=255)),
                ('municipality', models.CharField(default='None', max_length=255)),
                ('postal_code', models.CharField(default='None', max_length=10)),
                ('neighborhood', models.CharField(default='None', max_length=100)),
                ('street_address', models.CharField(default='None', max_length=255)),
                ('exterior_number', models.CharField(default='None', max_length=10)),
                ('interior_number', models.CharField(blank=True, default='None', max_length=10, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
