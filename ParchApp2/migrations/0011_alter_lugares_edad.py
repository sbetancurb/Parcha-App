# Generated by Django 4.1.6 on 2023-03-19 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ParchApp2', '0010_remove_lugares_cat_lugares_categoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugares',
            name='edad',
            field=models.CharField(blank=True, choices=[('menor de edad', 'menor de edad'), ('mayor de edad', 'mayor de edad')], default='', max_length=50),
        ),
    ]
