# Generated by Django 4.1.2 on 2022-11-03 22:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_bd_familiares_edad'),
    ]

    operations = [
        migrations.AddField(
            model_name='bd_familiares',
            name='fecha',
            field=models.DateField(default=1, verbose_name=datetime.datetime.now),
            preserve_default=False,
        ),
    ]
