# Generated by Django 5.0.1 on 2024-03-04 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0014_alter_opcionpartefisicamotora_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opcionpartefisicamotora',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='opcionparteintelectual',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='opcionpartepsiquica',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
