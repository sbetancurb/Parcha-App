# Generated by Django 4.1.6 on 2023-03-20 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ParchApp2', '0011_alter_lugares_edad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugares',
            name='categoria',
            field=models.CharField(choices=[('Discoteca', 'Discoteca'), ('Restaurante', 'Restaurante'), ('Mirador', 'Mirador')], max_length=50),
        ),
        migrations.AlterField(
            model_name='lugares',
            name='descripcion',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='lugares',
            name='edad',
            field=models.CharField(choices=[('menor de edad', 'menor de edad'), ('mayor de edad', 'mayor de edad')], max_length=50),
        ),
    ]
