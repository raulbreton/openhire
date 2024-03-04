# Generated by Django 5.0.2 on 2024-03-04 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_offers', '0010_alter_joboffer_max_salary_alter_joboffer_min_salary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joboffer',
            name='brazo_derecho',
        ),
        migrations.RemoveField(
            model_name='joboffer',
            name='brazo_izquierdo',
        ),
        migrations.RemoveField(
            model_name='joboffer',
            name='cuello',
        ),
        migrations.RemoveField(
            model_name='joboffer',
            name='espalda',
        ),
        migrations.RemoveField(
            model_name='joboffer',
            name='mano_derecha',
        ),
        migrations.RemoveField(
            model_name='joboffer',
            name='mano_izquierda',
        ),
        migrations.RemoveField(
            model_name='joboffer',
            name='oido',
        ),
        migrations.RemoveField(
            model_name='joboffer',
            name='pie_derecho',
        ),
        migrations.RemoveField(
            model_name='joboffer',
            name='pie_izquierdo',
        ),
        migrations.RemoveField(
            model_name='joboffer',
            name='pierna_derecha',
        ),
        migrations.RemoveField(
            model_name='joboffer',
            name='pierna_izquierda',
        ),
        migrations.RemoveField(
            model_name='joboffer',
            name='sistema_cardiovascular',
        ),
        migrations.RemoveField(
            model_name='joboffer',
            name='sistema_neurologico',
        ),
        migrations.RemoveField(
            model_name='joboffer',
            name='sistema_neurologico_sistema_nervioso_periferico',
        ),
        migrations.RemoveField(
            model_name='joboffer',
            name='sistema_respiratorio',
        ),
        migrations.RemoveField(
            model_name='joboffer',
            name='tacto',
        ),
        migrations.RemoveField(
            model_name='joboffer',
            name='vista',
        ),
        migrations.AddField(
            model_name='joboffer',
            name='adaptaciones_fisicaMotora',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='joboffer',
            name='adaptaciones_intelectual',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='joboffer',
            name='adaptaciones_psiquica',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='joboffer',
            name='adaptaciones_sensorial',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='joboffer',
            name='afectacion_fisicaMotora',
            field=models.CharField(blank=True, choices=[('Leve', 'Leve'), ('Moderada', 'Moderada'), ('Grave', 'Grave')]),
        ),
        migrations.AddField(
            model_name='joboffer',
            name='afectacion_sensorial',
            field=models.CharField(blank=True, choices=[('Leve', 'Leve'), ('Moderada', 'Moderada'), ('Grave', 'Grave')]),
        ),
        migrations.AddField(
            model_name='joboffer',
            name='descripcion_fisicaMotora',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='joboffer',
            name='descripcion_intelectual',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='joboffer',
            name='descripcion_psiquica',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='joboffer',
            name='descripcion_sensorial',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='joboffer',
            name='independencia',
            field=models.CharField(blank=True, choices=[('Leve', 'Leve'), ('Moderada', 'Moderada'), ('Grave', 'Grave')]),
        ),
        migrations.AddField(
            model_name='joboffer',
            name='opcion_fisicaMotora',
            field=models.CharField(blank=True, choices=[('Brazos', 'Brazos'), ('Manos ', 'Manos '), ('Dedos', 'Dedos'), ('Piernas', 'Piernas'), ('Pies', 'Pies'), ('Columna Vertebral', 'Columna Vertebral'), ('Tronco', 'Tronco')]),
        ),
        migrations.AddField(
            model_name='joboffer',
            name='opcion_intelectual',
            field=models.CharField(blank=True, choices=[('Memoria', 'Memoria'), ('Razonamiento Lógico', 'Razonamiento Lógico'), ('Habilidades Sociales', 'Habilidades Sociales'), ('Habilidades Motoras', 'Habilidades Motoras'), ('Aprendizaje Académico', 'Aprendizaje Académico')]),
        ),
        migrations.AddField(
            model_name='joboffer',
            name='opcion_psiquica',
            field=models.CharField(blank=True, choices=[('Trastornos del Estado de Ánimo', 'Trastornos del Estado de Ánimo'), ('Trastornos de Ansiedad', 'Trastornos de Ansiedad'), ('Trastornos de la Personalidad', 'Trastornos de la Personalidad')]),
        ),
        migrations.AddField(
            model_name='joboffer',
            name='opcion_sensorial',
            field=models.CharField(blank=True, choices=[('Visual', 'Visual'), ('Manos ', 'Manos '), ('Dedos', 'Dedos')]),
        ),
    ]