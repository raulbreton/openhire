# Generated by Django 5.0.1 on 2024-02-26 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_applications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='fecha_fin',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='fecha_inicio',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='recent_job_company',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='recent_job_title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='status',
            field=models.CharField(choices=[('Enviado', 'Enviado'), ('Interesado', 'Interesado'), ('En Revisión', 'En Revisión'), ('No Interesado', 'No Interesado')], default='Enviado', max_length=20),
        ),
    ]
