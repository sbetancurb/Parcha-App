# Generated by Django 4.1.6 on 2023-05-21 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ParchApp2', '0019_rename_urlbi_lugar_urlubi'),
    ]

    operations = [
        migrations.CreateModel(
            name='cuestionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Edad', models.CharField(choices=[('menor de edad', 'menor de edad'), ('mayor de edad', 'mayor de edad')], default='', max_length=50)),
                ('Zona', models.CharField(choices=[('Envigado', 'Envigado'), ('Poblado', 'Poblado')], default='', max_length=50)),
                ('Tipo', models.CharField(choices=[('Discoteca', 'Discoteca'), ('Restaurante', 'Restaurante'), ('Mirador', 'Mirador'), ('Centro Comercial', 'Centro Comercial')], default='', max_length=50)),
                ('Eco', models.CharField(choices=[('menor que 50k', 'menor que 50k'), ('entre 50k y 150k', 'entre 50k y 150k'), ('mas de 150k', 'mas de 150k')], default='', max_length=50)),
            ],
        ),
    ]