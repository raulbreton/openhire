# Generated by Django 5.0.1 on 2024-02-22 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_offers', '0007_remove_joboffer_municipality_joboffer_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joboffer',
            name='job_type',
            field=models.CharField(choices=[('Tiempo Completo', 'Tiempo Completo'), ('Medio Tiempo', 'Medio Tiempo'), ('Becario', 'Becario'), ('Temporal', 'Temporal'), ('Contrato', 'Contrato')], default='Tiempo Completo', max_length=20, null=True),
        ),
    ]
