# Generated by Django 5.0.2 on 2024-03-04 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_applications', '0003_alter_jobapplication_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='status',
            field=models.CharField(choices=[('Interesado', 'Interesado'), ('En Revisión', 'En Revisión'), ('No Interesado', 'No Interesado')], default='En Revisión', max_length=20),
        ),
    ]
