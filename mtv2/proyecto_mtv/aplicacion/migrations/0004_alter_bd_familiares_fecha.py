# Generated by Django 4.1.2 on 2022-11-03 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_bd_familiares_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bd_familiares',
            name='fecha',
            field=models.DateField(),
        ),
    ]
