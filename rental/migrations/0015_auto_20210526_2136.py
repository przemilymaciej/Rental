# Generated by Django 3.2 on 2021-05-26 19:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0014_auto_20210526_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookrenthistory',
            name='back_date',
            field=models.DateField(default=datetime.datetime(2021, 6, 25, 21, 36, 10, 825232)),
        ),
        migrations.AlterField(
            model_name='cdrenthistory',
            name='back_date',
            field=models.DateField(default=datetime.datetime(2021, 6, 25, 21, 36, 10, 829226)),
        ),
        migrations.AlterField(
            model_name='filmrenthistory',
            name='back_date',
            field=models.DateField(default=datetime.datetime(2021, 6, 25, 21, 36, 10, 827197)),
        ),
    ]