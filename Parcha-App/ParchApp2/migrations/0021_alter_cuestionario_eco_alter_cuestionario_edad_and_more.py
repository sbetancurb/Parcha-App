# Generated by Django 4.1.6 on 2023-05-21 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ParchApp2', '0020_cuestionario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuestionario',
            name='Eco',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cuestionario',
            name='Edad',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cuestionario',
            name='Tipo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cuestionario',
            name='Zona',
            field=models.CharField(max_length=50),
        ),
    ]
