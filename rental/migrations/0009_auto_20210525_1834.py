# Generated by Django 3.2 on 2021-05-25 16:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0008_auto_20210525_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookrenthistory',
            name='back_date',
            field=models.DateField(default=datetime.datetime(2021, 6, 24, 18, 34, 39, 971933)),
        ),
        migrations.AlterField(
            model_name='filmrenthistory',
            name='back_date',
            field=models.DateField(default=datetime.datetime(2021, 6, 24, 18, 34, 39, 972933)),
        ),
    ]
